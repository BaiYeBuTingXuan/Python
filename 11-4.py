from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy import poly1d,polyfit #polyfit 生成一组多项式系数，poly1d则根据系数返回一个多项式函数
from numpy.core.function_base import linspace
import pandas as pd

I0 = pd.DataFrame([0.0,1.0,2.0,3.0,4.0,5.0],dtype='float')
I1 = pd.DataFrame([0.0,1,2.07,3.06,3.97,4.97],dtype='float')
deltaI = I1-I0

x = np.array(I0)
y = np.array(deltaI)


plt.scatter(I0,deltaI,c='k',s=25,marker='x')
plt.plot(x,y,'k--')
plt.xlim(0,5.0)
plt.ylim(-0.1,0.1)
plt.xticks([1,2,3,4,5])
plt.xlabel('Ideal Volt/$V$')
plt.ylabel('Correction Volt/$V$')

plt.xlabel('\t \t \t \t \t \t \t \t \t \t \t \t Ideal Volt/$V$')
plt.ylabel('Error/$V$')

axes=plt.gca()  #gca:get current axis得到当前轴

#设置图片的右边框和上边框为不显示
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')

#挪动x，y轴的位置，也就是图片下边框和左边框的位置


axes.spines['bottom'].set_position(('data',0))  #data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
axes.spines['left'].set_position(('data',0))  #axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点


plt.title("FIGURE: Volt Error")

plt.savefig('d:\python\Python_workspace\physics\\figure11-4.png')


plt.show()