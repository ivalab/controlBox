from controlBox import ControlBox
from robotArmClass import RobotArm
from piktul import Piktul
from time import sleep
arm = Piktul('COM3', 9600)

arm.connect()
arm.setArm([-65,0,0,0,0],25)
sleep(3)
arm.setArm([65,65,65, 65, 65],25)
sleep(3)
arm.setArm([0,0,0,0,0],25)
sleep(3)
arm.setArm([-65,-65,0,0,0],25)
sleep(3)
arm.gotoHome()
sleep(3)
arm.shutDown()

    
