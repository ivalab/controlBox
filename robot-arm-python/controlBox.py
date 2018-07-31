''' @brief ControlBox class which sets up the control box on a general level
    @author Eduige Kayigirwa
    @date July 2018
    
'''

import serial
import numpy as np
import scipy as sci
from scipy.interpolate import interp1d
from time import sleep


class ControlBox:
    
    ## The constructor.
    ## @param portName is the serial port connected
    ## @param baud represents the baudrate 
    def __init__ (self, portName, baud):
        self.ser = serial.Serial()
        self.ser.port = portName
        self.ser.baudrate = baud
        
        
    ## the method to connect the control box to the computer
    ## @param self is the object pointer 
    def connect(self):
        self.ser.open()

    ## setServos method to move the servor    
    ## @param mid is the id number connected to the motor
    ## @param mcmd is the rotation direction of the motor     
       
    def change_int_to_list(self, num):
        myList = []
        if isinstance(num,int):
            myList.append(num)
            num = myList
            return num
    def setServos(self, alphaIds, command, speed = 25):
        
        # check if the arguments are integers or lists
        AlphaInt = []
        CommandInt = []
        if isinstance (alphaIds, int):
           alphaIds = self.change_int_to_list(alphaIds)

        if isinstance (command, int):
            command = self.change_int_to_list(command)
            
        if speed >0 and speed < 256:
            if len(alphaIds) == len(command):
                for i,m in zip(alphaIds, command):
                    serialCmd = 'E;m.'+str(i)+'.'+str(m) + '.'+str(speed) + ';'
                    #print ('{}'.format('E;m.'+str(i)+'.'+str(m) + ';'))
                    self.ser.write(serialCmd.encode())
           
        else:
            print ("speed must be between 0 and 255.")
    ## digitalIn method to allow data input
    ## returns [pins value], [raw values]
    ## @param function precise what to do with arguments
    ## @alphaIds is a list of servos you want to communicate to
    def digitalIn(self, function, alphaIds):
        pins = []
        outValues = []
        if function == 'i':
            for i in alphaIds:
                self.ser.write('{}'.format('a.'+str(function)+'.'+str(i) + ';'))
                outPut = self.ser.readline()
                #pins.append(outPut[10])
                outValues.append(int(outPut[15]))
                
            return (outValues)
            
        else:
            print ("The function " + '{}'.format(function).upper() +  " does not exist.")

    ## analogIn method to allow data input
    ## returns [pins value], [raw values], [converted values]
    ## @param function precise what to do with arguments
    ## @alphaIds is a list of servos you want to communicate to
    def analogIn(self, function, alphaIds):
        pins = []
        rawVals = []
        conVals = []
        if function == 'a':
            for i in alphaIds:
                self.ser.write('{}'.format('E;a.'+str(function)+'.'+str(i) + ';'))
                print ("from analog Input -----")
                outPut = self.ser.readline()
                # get just the pins and their 1s and 0s
                pins.append(outPut[10])
                rawVals.append(outPut[15:19])
                conVals.append(outPut[21:25])
            return (pins, rawVals, conVals)
                
        else:
            print ("The function " + '{}'.format(function).upper() +  " does not exist.")

    ## digitalOut method to writes output commands to serial port
    ## @param function precise what to do with arguments
    ## @param d_output precise one pin output to operate on
    ## @param is_on is a boolean value
    def digitalOut(self, d_outPut, is_on):
        serialCmd = 'o.' + str(d_outPut) + '.' + str(is_on)+ ';'
        self.ser.write(serialCmd.encode())
        #self.ser.write('{}'.format('o.' + str(d_outPut) + '.' + str(is_on) + ';'))
        reply = self.ser.readline()
        #print '{}'.format('o.' + str(d_outPut) + '.'+ str(is_on)+  ';')
                

    ## digitalOutList method to writes output commands to serial port
    ## @param function precise what to do with arguments
    ## @param dOutputList is a list of pins output to operate on
    ## @param is_on is a boolean value
    def digitalOutList(self, dOutputList, is_on):
        for dOut, val in zip(dOutputList, is_on):
            self.ser.write('{}'.format('o.' + str(dOut) + '.' + str(val) + ';'))
            self.ser.readline()
   
    ## disable method disables the robot
    def disable(self):
        self.ser.write('{}'.format('D;'))
            
    ## the method to close the port    
    def shutDown(self):
        self.ser.close()

    ## static method to calibrate the robot Arm
    @staticmethod
    def debugger():
        ser = serial.Serial('COM3', 9600)
        ser.write('{}'.format(';'))     






