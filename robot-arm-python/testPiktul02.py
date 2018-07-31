from controlBox import ControlBox
from robotArmClass import RobotArm
from piktul import Piktul
from time import sleep


def move(height, shoulder, joint, wrist, fingers):
    myArm = Piktul('COM3', 9600)
    myArm.connect()
    myArm.setArm([height, shoulder, joint, wrist, fingers], 25)
    sleep(3)
    #myArm.gotoHome()
    myArm.shutDown()

timer = 0
while timer != 120:
    
    height = raw_input("Height Position: ")
    shoulder = raw_input("Shoulder: ")
    joint = raw_input("Joint: ")
    wrist = raw_input("Wrist: ")
    fingers = raw_input("Fingers: ")

    move(int(height), int(shoulder), int(joint), int(wrist), int(fingers))

    sleep(2)
    timer+= 2


