import scipy as sci
from scipy.interpolate import interp1d
import numpy as np

from controlBox import ControlBox
from robotArmClass import RobotArm

class Piktul(ControlBox, RobotArm):

    def __init__(self, portName, baud):
        ControlBox.__init__(self, portName, baud)
        
        self.alphaIds = [1,2,3,4,5]
        self.alphaLims = np.array([ -90, -90, -90, -90, -90, 0.00,		
                                      0,   0,   0,   0,   0, 3.0/4.0,
                                   90,  90,  90,  90,  80, 1.125])
        self.alphaLims.shape = (3,6)

        self.musecLims = np.tile([[1000], [1500], [2000]], len(self.alphaIds))
        
        '''self.musecLims = np.array([ 525, 640, 860, 580, 790, 1475,			
               1460, 1520, 1725, 1455, 1580, 1760,			
               2320, 2400, 2500, 2340, 2500, 2500])
        self.musecLims.shape = (3,6) '''

        self.alphaHome = [0,0,0,0,0]
        self.alphaSleep = [0,0,0,0,0]
