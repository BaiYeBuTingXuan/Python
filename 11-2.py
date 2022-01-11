from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
from numpy.core.records import array
import pandas as pd

I0 = pd.DataFrame([0.0,1.0,2.0,3.0,4.0,5.0],dtype='float')
I1 = pd.DataFrame([0.0,1.05,1.95,2.90,3.83,4.94],dtype='float')
deltaI = I1-I0
print(deltaI)
x = np.array(I0)
y = np.array(deltaI)

plt.scatter(I0,deltaI,s=25,c='k',marker='x')
plt.plot(x,y,'k--')

plt.xlim(0,5.5)
plt.ylim(-0.2,0.2)
plt.xticks([1,2,3,4,5])
plt.xlabel('\t \t \t \t \t \t \t \t \t \t \t \t Ideal Current/$mA$')
plt.ylabel('Error/$mA$')

axes=plt.gca()  #gca:get current axis得到当前轴

#设置图片的右边框和上边框为不显示
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')

#挪动x，y轴的位置，也就是图片下边框和左边框的位置


axes.spines['bottom'].set_position(('data',0))  #data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
axes.spines['left'].set_position(('data',0))  #axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点


plt.title("FIGURE: Current Error")
plt.savefig('d:\python\Python_workspace\physics\\figure11-2.png')


plt.show()