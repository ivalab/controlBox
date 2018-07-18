from controlBox import ControlBox
from time import sleep

myBox = ControlBox('COM3', 9600)
myBox.connect()

timer = 0

dvals = myBox.digitalIn('i', [1,2,3])
print dvals
print len(dvals)
while timer != 30:
    myBox.digitalOutList(dvals[0], dvals[1])
    sleep(1)
    timer += 1


print ('Done')
myBox.digitalOutList(dvals[0], [0]*len(dvals[0]))
myBox.shutDown()


