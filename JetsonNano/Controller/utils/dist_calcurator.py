import os
import numpy as np
from enum import Enum

class DistFormula(Enum):
    T = 2.6
    F = 0.315
    IMG_ELEMENT = 0.00028
    K = 2925
    
class AngleFormula(Enum):
    ServoMax = 180
    WidthMax = 1080
    HightMax = 720

class AngleRange(Enum):
    WMax = 100
    WMin = 20
    HMax = 120
    HMin = 20
    
def Xangle2duty(Xcoordinate):
    deg = Xcoordinate / (AngleFormula.WidthMax.value/AngleFormula.ServoMax.value)
    return np.round(deg, decimals=2)

def Yangle2duty(Ycoordinate):
    deg = Ycoordinate / (AngleFormula.HightMax.value/AngleFormula.ServoMax.value)
    #deg = (AngleRange.HMax.value + AngleRange.HMin.value) - deg
    return np.round(deg, decimals=2)


def distance_formula(disparity):
    T=2.6
    f = 0.315
    img_element = 0.0001*2.8
    K = int(T*f/img_element)
    return K/disparity
    

def prams_calcurator(disparity, x, y):
    distance = DistFormula.K.value / disparity   #  disranse_formula(disparity)
    dcX, dcY = Xangle2duty(x), Yangle2duty(y)
    return np.round(distance, decimals=2), np.round(dcX, decimals=2), np.round(dcY, decimals=2)
 


