from controlBox import ControlBox
from time import sleep

myBox = ControlBox('COM3', 9600)
myBox.connect()

myBox.digitalOut(1,1)
for i in range(6):
    myBox.digitalOut(1, 1)
    sleep(1)
    myBox.digitalOut(1,0)
    sleep(1)
