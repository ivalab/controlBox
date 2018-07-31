''' @brief RobotArm class which inherits the ControlBox and manipulate the Robot Arm
    @author Eduige Kayigirwa
    @date July 2018
    
'''

from controlBox import ControlBox
import serial
import numpy as np
import scipy as sci
from scipy.interpolate import interp1d
import numpy as np


class RobotArm (ControlBox):
    ## The Constructor.
    ## @param portName is the serial port connected
    ## @param baud represents the baudrate
    ## @param alphaIds are the outlet to the motors servos
    def __init__(self, portName, baud, alphaIds):
        ControlBox.__init__(self,portName, baud)
        
        # if alphaIds is a single interger, change it to a list
        if isinstance(alphaIds, int):
            alphaIds = self.change_int_to_list(alphaIds)
            
        self.alphaIds = alphaIds
        self.alphaLims = np.tile( [[-90],[ 0], [90]], len(alphaIds))
        self.musecLims = np.tile( [[600], [1500], [2400]], len(alphaIds))
        self.alphaOrient = [-1,1,1,-1,1,-1]
        self.alphaHome = [0,0,0,0,0,0]
        self.alphaSleep = [0,0,0,0,0,0]

        #interpolation of angles to positions
        self.ticks = [0]*len(self.alphaIds)       
        
        for i in range(len(alphaIds)):
            # creates an object
            self.ticks[i] = interp1d(self.alphaLims[:,i], self.musecLims[:,i], fill_value = "extrapolate")
        


    ## a method to change the position of the servos with an optional speed 
    ## @param mid is the servos ids
    ## @param speed is optional to precise the speed of motion
    ## @param degrees is a list of degrees which are changed to a position
    
    def setArm(self, degrees, speed = 25):
        
        if isinstance((degrees), int):
            degrees = self.change_int_to_list(degrees)
        # a list of commands
        command = [0]*len(self.alphaIds)

        # make a degree list equal to alphaIds
        # helps not run out of index of degrees if they are less than alphaIds
        # or to run out of alphaIds
        # useful for the pathMapper
        if len(degrees) < len(self.alphaIds):
            newDeg = [0]*len(self.alphaIds)
            for j in range(len(degrees)):
                newDeg[j] = degrees[j]
            degrees = newDeg
            
        for i in range(len(self.alphaIds)): 
            command[i] = int(self.ticks[i](degrees[i]))
            #print degrees[i]
            #print (command[i])
           
        self.setServos(self.alphaIds, command, speed)

    
    ## method setJoint changes the position of the servos angles
    ## @param alphaIds is a list of servos ids
    ## @param speed is optional to precise the speed of motion
    ## @param degrees is a list of degrees the servos rotate by

    def setJoint(self, alphaIds, degrees, speed=255):
        if isinstance((degrees), int):
            degrees = self.change_int_to_list(degrees)
        # a list of commands
        command = [0]*len(self.alphaIds)

        # make a degree list equal to alphaIds
        # helps not run out of index of degrees if they are less than alphaIds
        # or to run out of alphaIds
        # useful for the pathMapper
        
        newDeg = [0]*len(self.alphaIds)
        for j in range(len(degrees)):
            newDeg[j] = degrees[j]
        degrees = newDeg
        
        for i in range(len(self.alphaIds)):
            # to test if the setArm works            
            command[i] = int(self.ticks[i](degrees[i]))           
                
        self.setServos(alphaIds, command, speed)

    ## method gotoHome puts the robot arm to its default state
    ## @param speed is option and is 25 by default
    def gotoHome(self, speed=25):
        print (self.alphaHome[:6])
        self.setArm(self.alphaHome, speed)

    
    def  gotoSleep(self, speed=15):
        self.setArm(self.alphaSleep, speed)

    ## method setAlphaLims allows the change of alphaLims
    ## @param newAlphaLims are the new coordinate you want for the alphaLims
    def setAlphaLims(self, newAlphaLims):
        if isinstance(newAlphaLims, int):
            makeList = []
            makeList.append(newAlphaLims)
            newAlphaLims = makeList
        else:
            pass
        # to make newAlphalims a one-column vector
        outL = []
        for element in newAlphaLims:
            subL = []
            subL.append(element)
            outL.append(subL)
            
        self.alphaLims = outL
        #print (self.alphaLims)
        
    ## method setMusecLims allows the change of alphaLims
    ## @param newMusecLims are the new coordinate you want for the alphaLims    
    def setMusecLims(self, newMusecLims):
        if isinstance(newMusecLims, int):
            makeList = []
            makeList.append(newMusecLims)
            newMusecLims = makeList
        else:
            pass
        # to make newMusecLims a one-column vector
        outM = []
        for el in newMusecLims:
            subM = []
            subM.append(el)
            outM.append(subM)
            
        self.musecLims = outM
        #print (self.musecLims)
        

        
