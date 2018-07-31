## scripts to test the ControlBox calibrating static method
from controlBox import ControlBox

test = ControlBox('COM3', 9600)
test.connect()
test.setServos(1, 1500, 25)
#test.disable()
test.shutDown()

print ControlBox.debugger()

