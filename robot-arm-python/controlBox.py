
import serial
import numpy as np
import scipy as sci
from scipy.interpolate import interp1d

## Documentation for class ControlBox

class ControlBox:
    # class properties
    alphaLims = np.array([-90,0,90])
    musecLims = np.array([512,1600,2437])
    
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

    ## setServos method to move the servor    
    ## @param mid is the id number connected to the motor
    ## @param mcmd is the rotation direction of the motor     
       

    def setServos(self,mid, mcmd, speed = 255):
        if speed >0 and speed < 256:
            if len(mid) == len(mcmd):
                for i,m in zip(mid, mcmd):
                    #print ('"{}"'.format('E;m.'+str(i)+'.'+str(m) + ';'))
                    self.ser.write('"{}"'.format('E;m.'+str(i)+'.'+str(m) + ';'))
            # what to do if there is no motor connected to the id?
            #what happens if there is more ids than connected motors?
        else:
            print "speed must be between 0 and 255."

    def digitalIn(self, function, mid):
        if function == 'a' or function == 'i':
            for i in mid:
                self.ser.write('"{}"'.format('E;a.'+str(function)+'.'+str(i) + ';'))
        else:
            print "The function " + '"{}"'.format(function).upper() +  " does not exist."

    def digitalOut(self, d_outPut, is_on):
        if is_on == 1 or is_on == 0:
            self.ser.write('"{}"'.format('E;o.' + str(d_outPut) + str(is_on) + ';'))
        else:
            print ('Inappropriate Arguments')          
                
            
    # the method to close the port    
    def shutDown(self):
        self.ser.close()

    # a method to set the arm
    
    def setArm(self):
        ticks = interp1d(self.alphaLims, self.musecLims, axis = 0,
                         fill_value = "extrapolate")
        print "These are the angles and corresponding positions"



