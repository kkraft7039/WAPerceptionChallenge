"""
This script reads the image of a lane outlined by cones and draws the lines
of the edges of the lane based on where the cones are.

Author: Kailan Kraft
Email: kmkraft2@wisc.edu
"""

import numpy as np
import cv2

# Load lane image
lane = cv2.imread('red.png')

# Grab width and height of image
height, width, _ = lane.shape

# Mask image using HSV
hsv = cv2.cvtColor(lane, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 180, 180])
upper_red = np.array([30, 230, 230])
mask = cv2.inRange(hsv, lower_red, upper_red)

# Find contours of detected cones
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract cone coordinates from contours
cone_centers = []
for cone in contours:
    x, y, w, h = cv2.boundingRect(cone)
    # Find center of cone
    center = (x + (w // 2), y + (h // 2))
    cone_centers.append(center)

# Find if cones are on left or right side of image
left_cones = []
right_cones = []
for cone in cone_centers:
    if cone[0] < (width//2):
        left_cones.append(cone)
    else:
        right_cones.append(cone)

# Length to draw both lines
line_length = 2000

# Grab left line parameters
left_cones = np.array(left_cones)
vx, vy, x0, y0 = cv2.fitLine(left_cones, cv2.DIST_L2, 0, 0.01, 0.01)

# Find start and end points of the left line
x1 = int(x0[0] - line_length * vx[0])
y1 = int(y0[0] - line_length * vy[0])
x2 = int(x0[0] + line_length * vx[0])
y2 = int(y0[0] + line_length * vy[0])

# Draw left line onto final image
cv2.line(lane, (x1, y1), (x2, y2), (0, 0, 255), 5)

# Grab right line parameters
right_cones = np.array(right_cones)
vx, vy, x0, y0 = cv2.fitLine(right_cones, cv2.DIST_L2, 0, 0.01, 0.01)

# Find start and end points of the right line
x1 = int(x0[0] - line_length * vx[0])
y1 = int(y0[0] - line_length * vy[0])
x2 = int(x0[0] + line_length * vx[0])
y2 = int(y0[0] + line_length * vy[0])

# Draw right line onto final image
cv2.line(lane, (x1, y1), (x2, y2), (0, 0, 255), 5)

# Save answer image with lane line
cv2.imwrite('answer.png', lane)

# Resize and display answer image
img = cv2.resize(lane, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()