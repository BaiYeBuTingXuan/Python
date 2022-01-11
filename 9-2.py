import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score

c = 2.99792458 # *10**8
e = 1.602 # *10**-19
h0 = 0.6626 # *10**-35
wave = pd.DataFrame([365,405,436,546,577],dtype='float')

f = c/wave*10**3

print(f)

u1 = [-1.830,-1.484,-1.268,-0.728,-0.622]
u2 = [-1.833,-1.482,-1.272,-0.718,-0.614]
u3 = [-1.833,-1.477,-1.266,-0.723,-0.611]

U = pd.DataFrame([u1,u2,u3],dtype='float',index=['u1','u2','u3'])

mean_U = pd.DataFrame(abs(U.mean(axis=0)))

print(mean_U)

pic=plt.figure(figsize=(8,6),dpi=80)


line=LinearRegression()
line.fit(f,mean_U)
alpha=line.intercept_[0] #截距
beta=line.coef_[0][0]   #斜率
# x=np.linspace(-0.5,13,2)
x1=np.linspace(3.7,13,2)
x2=np.linspace(-0.5,3.7,2)
y1=alpha+beta*x1
y2=alpha+beta*x2


print('斜率：', beta)
print('截距: ', alpha)

x_test=f
y_pre=alpha+beta*x_test
y_real=mean_U
print('线性回归模型的R^2=' , r2_score(y_pre,y_real))

plt.plot(x1,y1,'k-')
plt.plot(x2,y2,'k--')

plt.xlim(-0.1,14)
plt.ylim(-2.0,4.0)
# plt.xticks([1,2,3,4,5])
plt.xticks([1,5,9,13])
plt.yticks([-2,-1,1,2,3,4])
plt.xlabel('Frequency $Hz * 10^{14} $',)
plt.ylabel('Cutoff Voltage V')



plt.text(x=7.5,y=1.0,s='y={0:.3}'.format(beta)+'*$10^{-14}$'+'x{0:.3}\n$R^2$ = {1:.4}'.format(alpha,r2_score(y_pre,y_real))) #在任意位置显示文本


h = beta*e

E = abs(h-h0)/h0
print('h =',h)
print('E =',E)


axes=plt.gca()  #gca:get current axis得到当前轴

#设置图片的右边框和上边框为不显示
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')

#挪动x，y轴的位置，也就是图片下边框和左边框的位置


axes.spines['bottom'].set_position(('data',0))  #data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
axes.spines['left'].set_position(('data',0))  #axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点


plt.title("FIGURE 2 : Cutoff Voltage - Frequency")
plt.savefig(r"D:\\python\\Python_workspace\\physics\\9-2.png")
plt.show()
