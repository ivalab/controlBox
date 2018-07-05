from controlBox import ControlBox

myBox = ControlBox('COM3', 9600)
myBox.connect()
myBox.setServos([1,2,6],[1700,1700,600], 256)
myBox.digitalIn('f', [1,2])
myBox.digitalOut(1, 0)
myBox.setArm()
myBox.shutDown()
