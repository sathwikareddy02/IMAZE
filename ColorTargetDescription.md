# Hitting colored boxes in given order

TASK

Design a controller for an Autonomous robot that can hit the coloured boxes in the arena in the given order. The Bot should avoid other color boxes when trying to hit the target box in the arena. After hitting all the three coloured 
boxes ( For ex. Green, Violet, Blue), it
should reach Vision(RedBox) and
stop.To help you accomplish this task, you
are given a camera attached in front
side of the robot and distance
measuring sensors which can be used
to make Wanda move


DETAILS

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


BOT SPECIFICATIONS

E-puck
* BOT (Bot width =7.4 cm)
* we are using the robot, E-puck. It is a miniature two wheeled mobile robot originally developed at EPFL for teaching
  purposes.
* It has one forehead camera.
* It has 7 distance sensors of which you will be using only 4.
* There will be some set of functions to access the sensor values and control the wheels.
