''' @brief RobotArm class which inherits the ControlBox and manipulate the Robot Arm
    @author Eduige Kayigirwa
    @date July 2018
    
'''

import scipy as sci
from scipy.interpolate import interp1d
import numpy as np
from time import sleep
from controlBox import ControlBox
from robotArm import RobotArm

## Piktul class inherits from both the RobotArm and ControlBox
## changes robotArm attributes values
## Uses ControlBox methods to connect to the serial port
## You can use every method of the two parent classes here

class Piktul(ControlBox, RobotArm):

    def __init__(self, portName, baud):
        ControlBox.__init__(self, portName, baud)
        self.alphaIds = [1,2,3,4,5]
        self.alphaLims = np.array([ -90, -90, -90, -90, -90, 0.00,		
                                      0,   0,   0,   0,   0, 3.0/4.0,
                                   90,  90,  90,  90,  80, 1.125])
        self.alphaLims.shape = (3,6)

        self.musecLims = np.tile([[1000], [1500], [2000]], len(self.alphaIds))
        self.alphaOrient = [-1,-1, 1,1,-1]
        
        #interpolation of angles to positions (alphaLims to musec)
        self.ticks = [0]*len(self.alphaIds)       
        
        for i in range(len(self.alphaIds)):
            # creates an object
            self.ticks[i] = interp1d(self.alphaLims[:,i], self.musecLims[:,i], fill_value = "extrapolate")

        self.alphaHome = [0,0,0,0,0]
        self.alphaSleep = [0,0,0,0,0]

    def inchToDeg(self, inch, speed=25):
        
        if isinstance(inch, float) or isinstance(inch, int):
            inch = self.change_int_to_list(inch)

        inches = np.tile([[-1], [0], [1]], len(inch))
        ticks = [0]*len(inch)
        degree = [0]*len(inch)
        for i in range(len(inch)):
          ticks[i] = interp1d(inches[:,i], self.alphaLims[:,i], fill_value="extrapolate")
          #print ticks[i](inch[i])
          degree[i] = int(ticks[i]([inch[i]]))
        return degree
    
    def setMap(self, alphaPath, duration):
        if isinstance(alphaPath, list):
            lenAlpha = len(alphaPath)
            alphaPath = np.asarray(alphaPath)
            alphaPath.shape = (1, lenAlpha)
        rows = np.shape(alphaPath)[0]
            
        # to change the duration scalar into a list
        if isinstance(duration, float) or isinstance(duration, int):
            duration = self.change_int_to_list(duration)
        #print duration

        # make a list of duration which is equal to the lenght
        timer = [0]*len(self.alphaIds)
        for t in range(len(self.alphaIds)):
            if len(duration) == rows:
                timer[t] = duration[t]
                
            else:
                if len(duration) < rows:
                    lastD = len(duration)-1
                    timer[t] = duration[lastD]
                    
            
        print timer
        # the pathmapper goes through rows of joints angles matrix
        # self.alphaIds = 5... what if the columns are 3?
        # you run out of bound
        
        for i in range(len(self.alphaIds)):
    
            try:
                print alphaPath[:,i].tolist()
                print type(alphaPath[:,i].tolist())
                self.setArm(alphaPath[:, i].tolist())
                print timer[i]
                sleep(timer[i])
            # in case column of alphaPath Joint is less than actual AlphaIds
            except IndexError:
                break
        











        
                
