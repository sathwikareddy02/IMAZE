from controller import Robot,Motor,DistanceSensor
TIME_STEP = 2

MAX_SPEED = 6.28


robo = Robot()


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


while robo.step(TIME_STEP) != -1:
    
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    
    right_wall =  psValues[0]>180 or psValues[1] > 80.0 
    left_wall =  psValues[6] > 80.0 or psValues[7] > 80.0

    
    left_speed  =  MAX_SPEED
    right_speed =  MAX_SPEED
   
    if left_wall:
        
        left_speed  = .50 * MAX_SPEED
        right_speed = -0.250 * MAX_SPEED
    elif right_wall:
        
        left_speed  = -0.250 * MAX_SPEED
        right_speed = .5 * MAX_SPEED
    
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
  
