# Autonomous Obstacle Avoidance Robot and Implementing Object Detection Based on Color
This repository contains controller for 
* Autonomous Obstacle Avoidance Robot
* Implementing Object Detection Based on Color


## BOT SPECIFICATIONS

E-puck
* BOT (Bot width =7.4 cm)
* we are using the robot, E-puck. It is a miniature two wheeled mobile robot originally developed at EPFL for teaching
  purposes.
* It has one forehead camera.
* It has 7 distance sensors of which you will be using only 4.
* There will be some set of functions to access the sensor values and control the wheels.

## TASK for *Obstacle Avoidance Autonomous Bot* 

Design a controller for an Autonomous robot that can navigate through the maze. The Bot should have the ability to avoid any
kind of collision with the walls. To help you accomplish this task, you are given distance measuring sensors which can be
used to make your bot move.

### Additional details

The Bot should be fully autonomous.The Bot will start from the end of the maze and should spiral into its center.
There will be 4 distance sensors. Two in front, one at the left and one at the right. They will give the value of the 
distance of the wall in the specified direction they are at.The Bot should detect the walls and gaps using the distance
sensors and move through the gaps to complete the Maze.  <br />

### Simulation of the Obstacle avoidance bot controller using e-puck robot in Webots
Webots is an open source and multi-platform desktop application used to simulate robots.It provides a complete development environment to model, program and simulate robots.
It has been designed for a professional use, and it is widely used in industry, education and research. <br />

<img width="649" alt="image" src="https://user-images.githubusercontent.com/85176591/152930716-c7e28243-0f0c-4a18-b6a2-a7f6515c30e8.png"><br /><br />


## TASK for *Implementing Object Detection Based on Color* 

Design a controller for an Autonomous robot that can hit the coloured boxes in the arena in the given order. The Bot should avoid other color boxes when trying to hit the target box in the arena. After hitting all the three coloured 
boxes ( For ex. Green, Violet, Blue), it
should reach Vision(RedBox) and
stop.To help you accomplish this task, you
are given a camera attached in front
side of the robot and distance
measuring sensors which can be used
to make Wanda move

### Additional details

The task is to hit all the coloured
boxes present in the arena in the
same order they have been
arranged from left to right in the
arena.
For example there are 4 boxes
Green, Blue, Violet, Red kept in the
arena from left to right. Your bot
will start from the starting point in
the arena and then it has to detect
the first box from the left(Green)
using the image taken by the
forehead camera. It has to go and
hit the desired box avoiding other
boxes in the arena. For hitting a box it has to move near the box and stop at a
distance less than 20cm. Similarly it has to go and hit the other boxes(Blue,
Violet and Red) in the order they are arranged from left to right. After hitting all
the boxes the task will be completed.

### Implementing Object Detection Based on Color using e-puck robot in Webots
Here the bot targets and hits the objects in the order GREEN->BLUE->VOILET->RED and then stops by its own after the task.<br />

<img width="653" alt="image" src="https://user-images.githubusercontent.com/85176591/152931175-0fc22ce1-90f7-40fc-80d5-7c59bcc8c61e.png"><br /><br />

