from controlBox import ControlBox
from time import sleep

myBox = ControlBox('COM3', 9600)
myBox.connect()

timer = 0
while timer != 15:
    myBox.digitalIn('i',[1,2])
    sleep(1)
    timer += 1
else:  
    print ('done')
myBox.shutDown()


