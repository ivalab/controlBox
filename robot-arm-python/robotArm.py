from controlBox import ControlBox
import serial
import numpy as np
import scipy as sci
from scipy.interpolate import interp1d
import numpy as np

# inherits ControlBox class
class RobotArm (ControlBox):
    # class properties

    def __init__(self, portName, baud, alphaIds):
        ControlBox.__init__(self,portName, baud)
        self.alphaIds = alphaIds
        self.alphaLims = np.tile( [[-90],[ 0], [90]], len(alphaIds))
        self.musecLims = np.tile( [[600], [1500], [2400]], len(alphaIds))
        self.alphaHome = [0,0,0,0,0,0]
        self.alphaSleep = [0,0,0,0,0,0]
        
    #interpolation of angles to positions
        self.ticks = [0]*len(self.alphaIds)
        for i in range(len(alphaIds)):
            # creates an object
            self.ticks[i] = interp1d(self.alphaLims[:,i], self.musecLims[:,i], axis = 0,
                                 fill_value = "extrapolate")



    # a method to change the position of the servos with an optional speed 
    # @param mid is the servos ids
    # @param speed is optional to precise the speed of motion
    # @param degrees is a list of degrees which are changed to a position
    
    def setArm(self, degrees, speed = 255):
        command = [0]*len(self.alphaIds)
        for i in range(len(self.alphaIds)):
            # to test if the setArm works            
            command[i] = int(self.ticks[i](degrees[i]))          
            
        self.setServos(self.alphaIds, command, speed)
        
    # method setJoint changes the position of the servos angles
    # @param alphaIds is a list of servos ids
    # @param speed is optional to precise the speed of motion
    # @param degrees is a list of degrees the servos rotate by

    def setJoint(self, alphaIds, degrees, speed=255):
        command = [0]*len(self.alphaIds)
        for i in range(len(self.alphaIds)):
            # to test if the setArm works            
            command[i] = int(self.ticks[i](degrees[i]))           
            
        self.setServos(alphaIds, command, speed)        

    def gotoHome(self, speed=25):
        print self.alphaHome[:6]
        self.setArm(self.alphaHome, speed)

    def  gotoSleep(self, speed=15):
        # I think should use this to shut down the serial port as well
        self.setArm(self.alphaSleep, speed)
            

