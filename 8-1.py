import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score

V = pd.DataFrame([[86.43,66.05,56.52,40.04,29.00],[83.22,62.19,52.16,33.81,19.36]],dtype='float',index=['v1','v2'])

print(V)

v_mean =  pd.DataFrame(V.mean(axis=0))

print(v_mean)

a = pd.DataFrame([-5.80,-5.28,-5.06,-4.93,-4.79],dtype='float')


m = 188.8

F = m*a

print(a)
print(F)

pic=plt.figure(figsize=(8,6),dpi=80)

plt.scatter(v_mean,F,c='k',s=25,marker='x')
plt.xlim(24,88)
plt.ylim(-1100,-900)
# plt.xticks(np.arange(24,88,16))
plt.xlabel('Average of Velocity cm/s ')
plt.ylabel('$Net\\ Force \\ g·cm/s^{2}$')

line=LinearRegression()
line.fit(v_mean,F)
alpha=line.intercept_[0] #截距
beta=line.coef_[0][0]   #斜率
x=np.linspace(24,88,3)
y=alpha+beta*x

print('斜率：', beta)
print('截距: ', alpha)

x_test=v_mean
y_pre=alpha+beta*x_test
y_real=F
print('线性回归模型的R^2=' , r2_score(y_pre,y_real))

plt.plot(x,y,'k--')

plt.text(x=43,y=-1000,s="y=-3.04x-815\n$R^2$ = {0:.4}".format(r2_score(y_pre,y_real)))
plt.title("FIGURE: Net Force - Average of Velocity")
plt.savefig('d:\python\Python_workspace\physics\\figure8.png')
plt.show()

