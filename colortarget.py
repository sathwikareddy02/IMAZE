from controller import Robot,Motor,DistanceSensor,Camera
TIME_STEP = 2
import cv2
import numpy as np
MAX_SPEED = 6.28
robo = Robot()
camera=robo.getDevice("camera")
camera.enable(1)
ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
          ]

for i in range(8):
    ps.append(robo.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

left_motor = robo.getDevice('left wheel motor')
right_motor = robo.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
def moveright():
    global left_speed, right_speed,MAX_SPEED
    left_speed  = 0.50 * MAX_SPEED
    right_speed = -0.5 * MAX_SPEED
def moveleft():
    global left_speed, right_speed,MAX_SPEED
    left_speed  =-0.50* MAX_SPEED
    right_speed =0.50* MAX_SPEED
     
def moveforward():
     global left_speed, right_speed,MAX_SPEED
     left_speed  =MAX_SPEED*0.75
     right_speed =MAX_SPEED*0.75


k=0
left_speed=0
right_speed=0
while robo.step(TIME_STEP) != -1:
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())
   
    camera.saveImage("rgb.jpg",100)
    img = cv2.imread("rgb.jpg")
    img = cv2.resize(img, (200,200))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #RANGES

        #green
    lower_g = np.array([60, 40, 40])
    upper_g = np.array([100, 255, 255])
        #blue
    lower_b = np.array([115, 95, 95])
    upper_b = np.array([140, 255, 255])
        #voilet
    lower_v = np.array([130, 50, 50])
    upper_v = np.array([160, 255, 255])
        #red
    lower_r = np.array([160, 50, 50])
    upper_r = np.array([255, 255, 255])

    #masking
    red = cv2.inRange(hsv, lower_r, upper_r)
    blue = cv2.inRange(hsv, lower_b, upper_b)
    green = cv2.inRange(hsv, lower_g, upper_g)
    voilet = cv2.inRange(hsv, lower_v, upper_v)

    mask = [green,blue,voilet,red]

    cv2.imshow('img',img)
    
    cv2.waitKey(1)

    mass=np.sum(mask[k])
    if mass > 100000:
        moveforward()
    else:
        moveleft()
        
    if psValues[0] > 100 or psValues[7] > 100 or psValues[0] > 100 or psValues[0] > 100:
        k+=1
        t=robo.getTime()
        while robo.step(TIME_STEP) != -1:
            left_motor.setVelocity(-3)
            right_motor.setVelocity(-3)
            l=robo.getTime()
            if l > t+3.3:
                break
            pass
        t=robo.getTime()
        while robo.step(TIME_STEP) != -1:
            left_motor.setVelocity(3)
            right_motor.setVelocity(-3)
            l=robo.getTime()
            if l > t+0.2:
                break
            pass
        

       
    if k==4:
        break
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    pass
while robo.step(TIME_STEP) != -1:
            left_motor.setVelocity(0)
            right_motor.setVelocity(0)

            pass
