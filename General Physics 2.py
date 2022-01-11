from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
from numpy.core.records import array
import pandas as pd

data = np.array([656,486,434,410])

num = np.array([1,2,3,4,5])
num_ = np.array([2,3,4,5,6])

c = 912

res = c/data

print(res)