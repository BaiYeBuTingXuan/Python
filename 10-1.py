import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
import pandas as pd

T = pd.DataFrame([25.1,32.3,41.5,46.9,51.3,57.8,61.7,66.8],dtype='float')
mV = pd.DataFrame([37.5,45.9,56.5,62.5,67.4,74.3,78.6,84.0],dtype='float')

Us = 1300

alpha1 = 4*mV/(T*(Us-2*mV))

print(alpha1)
alpha = 0.004573
print(np.mean(alpha1))

x = linspace(20,70,40)
y = (alpha*x/(4+2*alpha*x))*Us

plt.scatter(T,mV,c='k',s=25,marker='x')
plt.plot(x,y,'k-')
plt.xlim(20,70)
plt.ylim(37,85)
# plt.xticks(np.arange(24,88,16))
plt.xlabel('Temperature /$^\circ$C')
plt.ylabel('Electric Resistance /$\Omega$')

plt.title("FIGURE: Temperature - Resistence")
plt.savefig('d:\python\Python_workspace\physics\\figure10-2.png')
plt.show()

