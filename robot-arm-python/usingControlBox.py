from controlBox import ControlBox
from robotArm import RobotArm

myBox = ControlBox('COM3', 9600)
myBox.connect()
#myBox.setServos([1,2,6],[1000,600,1000], 17)
myBox.digitalIn('f', [1,2])
myBox.digitalOut(1, 0)

myBox.shutDown()

myArm = RobotArm('COM3', 9600,[1,2,6])
myArm.connect()
myArm.setServos([3,4],[900,900], 25)
myArm.setServos([3,4],[1500,1500], 25)
myArm.setServos([3,4],[2000,2000], 25)
#myArm.setServos(1,2000, 25)


print (myArm.alphaIds)
myArm.setArm([0,0,0],25)
myArm.setArm([85,85,85],25)
myArm.setArm([0,0,0],25)
myArm.setArm([-85,-85,-85],25)
myArm.gotoHome()
myArm.shutDown()


'''
    write a reset static function to make the motors work
    It should send a bunch of ";" to the serial port and shut it down
    That way you 
'''
