from controlBox import ControlBox
from time import sleep

myBox = ControlBox('COM3', 9600)
myBox.connect()

timer = 0



while timer != 100:
    dvals = myBox.digitalIn('i', [1,2,3])
    print(dvals)
    myBox.digitalOutList([1, 2, 3], dvals)
    sleep(1)
    timer += 1

print ('Done')
myBox.digitalOutList([1, 2, 3], [0, 0, 0])
myBox.shutDown()


