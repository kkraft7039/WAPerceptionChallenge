# Wisconsin Autonomous Perception Challenge
This repository contains my final code for the Perception Team's coding challenge on Wisconsin Autonomous.

# Final Image
The answer.png resulting from the LaneTracker Python code
![alt text](answer.png)

# Methodolgy
To start with the coding challenge, I first had to learn OpenCV as I have had no prior experience with it. I decided to use Python as my language of choice as 
most people seem to use Python when using OpenCV, and it simplifies the process. I went through Tech With Tim's tutorials on OpenCV before diving into the
challenge. While watching the videos, I put some ideas together as to how I would go about separating the cones and creating the lines. Whenever I found myself
getting stuck, I would go into the documentation looking for other methods and Stackoverflow on how to use them.

# Challenges
The biggest challenge I ran into was drawing the lines using the cones. My initial plan was to use the top and bottom cones of each side to find the slope and draw
the line using one of the points and its slope. This proved to be difficult, however, when finding the start and end points of the line while staying inside of
the frame. I had to find the intercept the line would have with the side of the image and make sure it was still inside. This process felt like it would be too tedious
and unnecessary, so I decided to then look for a new method and found fitLine() which worked far better.

# Libraries
The two libraries I used were NumPy and OpenCV
