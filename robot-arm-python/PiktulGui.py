from controlBox import ControlBox
from robotArm import RobotArm
from piktul import Piktul
from time import sleep
from Tkinter import *
import numpy as np

# Input Validation
def InchChecker(inch, newInch):
    if inch < -1 or inch > 1:
        inch, newInch = newInch, inch
        return inch
    else:
        pass
        return inch

def angleChecker(angle, newAngle):
    if angle not in range (-90, 91):
        angle, newAngle = newAngle, angle
        return angle
    else:
        pass
        return angle

def changeToNumber(angle):
    try:
        angle = int(angle)
    except ValueError:
        angle = 0
    return angle

# The GUI set-up

root = Tk()
root.title("ROBOT ARM")

Height_label = Label(root, text= "HEIGHT: ")
Height_label.grid(row= 1, column= 1, padx= 100, pady=10)
Height = Entry(root)
Height.grid(row= 1, column = 3, padx= 10, pady=10)
Height.focus_set()


Shoulder_label = Label(root, text= "SHOULDER: ")
Shoulder_label.grid(row=2, column=1, padx= 10, pady=10)
Shoulder = Entry(root)
Shoulder.grid(row =2, column=3, padx= 10, pady=10)
Shoulder.focus_set()
    

Joint_label = Label(root, text="JOINT: ")
Joint_label.grid(row=3, column=1, padx= 10, pady=10)
Joint = Entry(root)
Joint.grid(row= 3, column= 3, padx= 10, pady=10)
Joint.focus_set()


Wrist_label = Label(root, text= "WRIST: ")
Wrist_label.grid(row= 4, column=1, padx= 10, pady=10)
Wrist = Entry(root)
Wrist.grid(row= 4, column= 3, padx= 10, pady=10)
Wrist.focus_set()


Finger_label = Label(root, text= "FINGERS: ")
Finger_label.grid(row=5, column=1, padx= 10, pady=10)
Fingers = Entry(root)
Fingers.grid(row= 5, column= 3, padx= 10, pady=10)
Fingers.focus_set()

# the command function
def moveAll():
    myArm = Piktul("COM3", 9600)
    myArm.connect()
    
    height = changeToNumber(Height.get())
    height = InchChecker(height, 1)
    height = myArm.inchToDeg(height)[0]
    
    shoulder = changeToNumber(Shoulder.get())
    shoulder = angleChecker(shoulder, 90)

    
    joint = changeToNumber(Joint.get())
    joint = angleChecker(joint, 90)

    wrist = changeToNumber(Wrist.get())
    wrist = angleChecker(wrist, 90)

    
    finger = changeToNumber(Fingers.get())
    finger = InchChecker(finger, 0)
    finger = myArm.inchToDeg(finger)[0]
    

    myArm.setArm([height*myArm.alphaOrient[0], shoulder*myArm.alphaOrient[1], joint*myArm.alphaOrient[2], wrist*myArm.alphaOrient[3], finger*myArm.alphaOrient[4]], 25)

    myArm.shutDown()

but_motion= Button(root, text= "MoveAll", command=moveAll)
but_motion.grid(row= 9, column=3, padx= 10, pady=10)
    

def shut_down():
    myArm = Piktul('COM3', 9600)
    myArm.connect()
    myArm.gotoHome()
    myArm.disable()
    myArm.shutDown()


but_disconnect = Button(root, text = "Disconnect The Arm", command = shut_down)
but_disconnect.grid(row= 12, column= 3, padx= 10, pady=10)

but_quit = Button(root, text= "Shut", command = quit)
but_quit.grid(row= 13, column= 3, padx= 10, pady=10)
root.mainloop()





