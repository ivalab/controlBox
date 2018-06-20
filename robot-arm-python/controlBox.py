
import serial

## Documentation for class ControlBox

class ControlBox:
    ## The constructor.
    def __init__ (self, portName, baud):
        self.ser = serial.Serial()
        self.ser.port = portName
        self.ser.baudrate = baud
        
    # the method of connecting
    # method Documentation
    #@param self is the object pointer 
    def connect(self):
        self.ser.open()

    ## setServor method to move the servor    
    ## @param mid is the id number connected to the motor
    ## @param mcmd is the rotation direction of the motor
        
    def setServor(self,mid, mcmd):
        if len(mid) == len(mcmd):
            for i,m in zip(mid, mcmd):
                self.ser.write('"{}"'.format('E;m.'+str(i)+'.'+str(m) + ';'))
        # what to do if there is no motor connected to the id?
        #what happens if there is more ids than connected motors?
        
    # the method to close the port    
    def shutDown(self):
        self.ser.close()

myBox = ControlBox('COM3', 9600)
myBox.connect()
myBox.setServor([1,2,6],[1600,2000,1000])
myBox.shutDown()

