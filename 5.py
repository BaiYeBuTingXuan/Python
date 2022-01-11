import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
from numpy.testing._private.utils import print_assert_equal
import pandas as pd

Up = pd.DataFrame([[59.7,65.0,70.0,75.0,75.5,76.0,76.4,76.9,77.5,78.0,78.5,79.0,79.5,80.0,80.7,81.1,81.5,82.1,82.5,82.9,83.5,84.0,84.5,85.0,85.5,89.4,93.6],
                    [48.4,48.4,47.5,37.9,36.9,35.4,34.1,32.8,31.2,29.8,28.6,27.2,26.3,24.7,23.2,22.1,21.4,20.5,19.8,19.0,18.0,17.3,16.5,15.8,15.3,11.6,9.1]],
                    index=['temperature','volt'],dtype='float')

Down = pd.DataFrame([[94.0,89.6,84.4,83.6,83.1,82.6,82.1,81.3,80.8,80.4,79.7,79.2,78.6,78.0,77.5,76.9,76.1,75.6,75.1,74.6,74.1,73.6,73.0,72.6,72.1,71.6,71.1,70.7,70.4,70.0,69.5,69.0,68.5,63.7,58.8],
                    [9.0,11.2,15.0,15.6,16.1,16.8,17.5,18.6,19.4,20.3,21.7,22.7,23.5,24.8,26.4,27.7,29.9,30.9,32.1,33.8,35.0,36.7,38.0,39.4,40.8,42.0,42.9,43.8,44.7,45.5,46.3,47.1,47.7,49.2,49.1]],
                    index=['temperature','volt'],dtype='float')

print(Up)

pic=plt.figure(figsize=(8,6),dpi=80)

plt.xlabel('Temperature (℃)')
plt.ylabel('Volt(mV)')
plt.xlim(58,95)
plt.ylim(8,50)
x = linspace(58,95,1000)

plt.scatter(Up.iloc[0,:],Up.iloc[1,:],c='k',s=20,marker='x')
plt.scatter(Down.iloc[0,:],Down.iloc[1,:],c='k',s=30,marker='+')

coeffup = polyfit(Up.iloc[0,:],Up.iloc[1,:],8)
f = poly1d(coeffup)
plt.plot(x,f(x),'k--')
print(coeffup)


coeffdown = polyfit(Down.iloc[0,:],Down.iloc[1,:],8)
g = poly1d(coeffdown)
plt.plot(x,g(x),'k-')

plt.legend(['$incre. curve$','$decre. curve$'])


f_ = np.polyder(f,1) #对多项式求导
rootf = np.roots(f_)

g_ = np.polyder(g,1)
rootg = np.roots(g_)

print("f_",rootf)
print("g_",rootg)



plt.savefig("d:\\python\\Python_workspace\\physics\\figure5.png")
plt.show()


