from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
import pandas as pd

I0 = pd.DataFrame([1,0.74,0.48,0.31,0.20,0.10,0.07,0.04,0.01,0],dtype='float')
R = pd.DataFrame([0,100,300,600,1000,2000,5000,8000,10000,20000],dtype='float')
E = 1500

I0 = I0*5

x = linspace(0.0001,5,1000)

y = E/x-280.3

plt.scatter(I0,R,c='k',s=25,marker='x')
plt.plot(x,y,'k--')
plt.xlim(0,5)
plt.ylim(0,25000)
plt.xticks([1,2,3,4,5])
plt.xlabel('Current Curve/$mA$')
plt.ylabel('Resistence/$\Omega$')

plt.title("FIGURE: Ohmmeter")
plt.savefig('d:\python\Python_workspace\physics\\figure11-5.png')


plt.show()