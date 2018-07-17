from controlBox import ControlBox
from robotArmClass import RobotArm
from piktul import Piktul
from time import sleep
arm = Piktul('COM3', 9600)


'''
 NOTE TO SELF:
 alphaId[0]-----> deals with height position
 alphaId[1]-----> deals with shoulder motion
 alphaId[2]-----> deals with joint motion
 alphaId[3]-----> deals with wrist motion
 alphaId[4](last one)-----> deals with fingers motion
'''
print ('Start the arm')
arm.connect()
sleep(5)
print('move arm up')
arm.setArm([-65,0,0,0,0],25) # moves in height (moves up)
sleep(5)
print ('move arm down')
arm.setArm([65,0,0,0,0],25) # moves in height (moves down)
sleep(5)

print ('go to home')
arm.setArm([0,0,0,0,0],25) # home position
sleep(5)

print 'move shoulder left'
arm.setArm([0,-65,0,0,0],25) # moved the shoulder
sleep(5)

print 'motion shoulder right'
arm.setArm([0,65,0,0,0],25) # moved the shoulder
sleep(5)

print ('go back to home')
arm.setArm([0,0,0,0,0],25) # home position
sleep(5)

print ('move joint left')
arm.setArm([0,0,65, 0, 0],25) # moved the joint 
sleep(5)

print ('move joint right')
arm.setArm([0,0,-65, 0, 0],25) # moved the joint
sleep(5)

print ('come back to home')
arm.setArm([0,0,0,0,0],25)  #home position
sleep(5)

print ('move wrist right')
arm.setArm([0,0,0,-65,0],25) 
sleep(5)

print ('move wrist left')
arm.setArm([0,0,0,65,0],25) 
sleep(5)

print ('come back to home')
arm.setArm([0,0,0,0,0],25) 
sleep(5)

print ('move fingers in')
arm.setArm([0,0,0, 0, 65],25) # moved the joint (to the left) and shoulder( to the right)
sleep(5)

print ('move fingers out')
arm.setArm([0,0,0, 0, -65],25) # moved the joint (to the left) and shoulder( to the right)
sleep(5)

print ('go back to home')
arm.setArm([0,0,0,0,0],25) 
sleep(5)

print ('GET CRAZY')
arm.setArm([65,65,65, 65, 65],25) # moved all direction (pretty crazy!)
sleep(5)


print 'move back home'
arm.gotoHome()
sleep(5)
print 'stay STill'
arm.shutDown()

    
