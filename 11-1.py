from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
import pandas as pd

I0 = pd.DataFrame([1.0,2.0,3.0,4.0,5.0],dtype='float')
I1 = pd.DataFrame([1.05,1.95,2.90,3.83,4.94],dtype='float')
deltaI = I1-I0

x = [0,5]


plt.scatter(I0,I1,c='k',s=25,marker='x')
plt.plot(x,x,'k--')
plt.xlim(0,5.0)
plt.ylim(0,5.0)
plt.xticks([1,2,3,4,5])
plt.xlabel('Ideal Current/$mA$')
plt.ylabel('Correction Current /$mA$')

plt.title("FIGURE: Current")
plt.savefig('d:\python\Python_workspace\physics\\figure11-1.png')


plt.show()