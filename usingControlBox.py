from controlBox import ControlBox
from robotArmClass import RobotArm

myBox = ControlBox('COM3', 9600)
myBox.connect()
myBox.setServos([1,2,6],[1600,1000,2000], 17)
myBox.digitalIn('f', [1,2])
myBox.digitalOut(1, 0)

myBox.shutDown()

myArm = RobotArm('COM3', 9600, [1,2,6])
myArm.connect()
#myArm.setServos([1,2,6],[2000,1200,1200], 255)
#myArm.setServos(myArm.alphaIds,[1600,600,2000], 25)


print myArm.alphaIds
myArm.setArm((5,85,-90), 255)
myArm.gotoHome()
myArm.shutDown()