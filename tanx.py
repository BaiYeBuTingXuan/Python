import numpy as np
from numpy.core.function_base import linspace
import pandas as pd
import matplotlib.pyplot as plt
import math

def fun(x):
    return np.tan(x) - x;

epsilon = 0.0001


a = 0
b = 1.57
sol = [0,0,0]

for i in [0,1,2]:
    x1 = a + i*np.pi
    x2 = b + i*np.pi

    while(abs(fun((x1+x2)/2)-0) > epsilon):
        if(fun((x1+x2)/2) < 0):
            x1 = (x1+x2)/2
        else:
            x2 = (x1+x2)/2
    
    sol[i] = (x1+x2)/2
    
print('sol:',sol)