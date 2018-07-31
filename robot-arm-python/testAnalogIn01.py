from controlBox import ControlBox
from time import sleep

myBox = ControlBox('COM3', 9600)
myBox.connect()

aVals = myBox.analogIn('a',[4,5,6])
print aVals
