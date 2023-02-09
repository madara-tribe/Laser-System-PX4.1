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
    DCMax = 12
    WidthMax = 640
    HightMax = 360


def Xangle2duty(Xcoordinate):
    deg = Xcoordinate / (AngleFormula.WidthMax.value/AngleFormula.ServoMax.value)
    dc = (deg*9.5)/AngleFormula.ServoMax.value + 2.5
    #print("x angle :{}, duty {}".format(deg, dc))
    return np.round(dc, decimals=2)

def Yangle2duty(Ycoordinate):
    deg = Ycoordinate / (AngleFormula.HightMax.value/AngleFormula.ServoMax.value)
    dc = (deg*9.5)/AngleFormula.ServoMax.value + 2.5
    #print("y angle :{}, duty {}".format(deg, dc))
    return np.round((AngleFormula.DCMax.value-dc), decimals=2)


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
 

