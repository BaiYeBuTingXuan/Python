import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score
    
F=pd.DataFrame([2.0,4.0,6.0,8.0,10,12,14,16,18])
L=pd.DataFrame([15,32,49,64,79,98,112,126,149])

pic=plt.figure(figsize=(8,6),dpi=80)

plt.scatter(L,F,c='k',s=25,marker='x')
plt.ylim(0,20)
plt.xlim(12,150)
plt.xticks(np.linspace(10,150,15))
plt.xlabel('Length (mm)')
plt.ylabel('Force (N)')


line=LinearRegression()
line.fit(L,F)
alpha=line.intercept_[0] #截距
beta=line.coef_[0][0]   #斜率
x=np.linspace(0,150,3)
y=alpha+beta*x

print('斜率：', beta)
print('截距: ', alpha)

x_test=L
y_pre=alpha+beta*x_test
y_real=F
print('线性回归模型的R^2=' , r2_score(y_pre,y_real))
plt.plot(x,y,'k-')

line.score(L,F)

plt.savefig('d:\python\Python_workspace\physics\\General1.png')
plt.show()