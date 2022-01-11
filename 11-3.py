from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
import pandas as pd

I0 = pd.DataFrame([1.0,2.0,3.0,4.0,5.0],dtype='float')
I1 = pd.DataFrame([1,2.07,3.06,3.97,4.97],dtype='float')
deltaI = I1-I0

x = [0,5]


plt.scatter(I0,I1,c='k',s=25,marker='x')
plt.plot(x,x,'k--')
plt.xlim(0,5.0)
plt.ylim(0,5.0)
plt.xticks([1,2,3,4,5])
plt.xlabel('Ideal Volt/$V$')
plt.ylabel('Correction Volt/$V$')

plt.title("FIGURE: Volt")
plt.savefig('d:\python\Python_workspace\physics\\figure11-3.png')


plt.show()