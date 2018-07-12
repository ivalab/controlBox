from controlBox import ControlBox
from robotArmClass import RobotArm
from time import sleep


myArm = RobotArm('COM3', 9600,[3,4])
myArm.connect()
myArm.setServos([3,4],[900,900], 25)
myArm.setServos([3,4],[1500,1500], 25)
myArm.setServos([3,4],[2000,2000], 25)
#myArm.setServos(1,2000, 25)


print myArm.alphaIds
myArm.setJoint([3,4],[0,0,0],25)
sleep(3)
myArm.setJoint([3,4],[65,0,0],25)
sleep(3)
myArm.setArm([-65,0,0],25)
sleep(3)
myArm.setArm([85,65,65],25)
sleep(3)
myArm.setArm([0,0,0],25)
sleep(3)
myArm.setArm([-85,-65,0],25)
sleep(3)
myArm.gotoHome()
sleep(3)
myArm.shutDown()


'''
    write a reset static function to make the motors work
    It should send a bunch of ";" to the serial port and shut it down
    That way you 
'''
