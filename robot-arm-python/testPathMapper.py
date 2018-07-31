import scipy as sci
from scipy.interpolate import interp1d
import numpy as np

from controlBox import ControlBox
from robotArm import RobotArm
from piktul import Piktul

A = Piktul('COM3', 9600)
A.connect()
deg = np.array([ -90, -90, -90, -90, -90,		
                    -90,   0,   0,   0,   0,
                    90,  90,  90,  90,  80,
                    -90, -90, 90, -90, -90,
                    -90, -90, 90, -90, -90
                    ])

deg.shape = (5,5)
inp = [-90,0,54]
A.setMap(inp, [1,2])
