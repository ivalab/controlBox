from controlBox import ControlBox
from time import sleep

myBox = ControlBox('COM3', 9600)
myBox.connect()

timer = 0
#while timer != 1:
    #myBox.analogIn('a',[4,5,6])
dvals = myBox.digitalIn('i', [1,2,3])
print dvals
print len(dvals)
while timer != 5:
    for el in dvals:
        print len(el)
        #print el.index(2)
        #print el.index(str(0))
        print el[10], el[15]
        myBox.digitalOut(el[10], el[15])

    sleep(1)
    timer += 1


print ('Done')

myBox.shutDown()


