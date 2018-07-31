from controlBox import ControlBox
from time import sleep


myBox = ControlBox('COM3', 9600)
myBox.debugger()
myBox.connect()

timing = 0
while timing != 15:
#for i in range(6):
    myBox.digitalOut(1, 1)
    myBox.digitalOut(2, 0)
    sleep(1)
    myBox.digitalOut(1,0)
    myBox.digitalOut(2,1)
    myBox.digitalOut(2,0)
    sleep(1)
    timing += 1

else:
    myBox.shutDown()
    print 'time_over'
