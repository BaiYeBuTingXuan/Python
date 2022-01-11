import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score
    
t=pd.DataFrame([12.5,17.5,22.5,27.6,32.6,37.8,42.8,47.5,52.4,57.6,62.6,67.6])
R=pd.DataFrame([0.4575,0.4676,0.4768,0.4863,0.4951,0.5044,0.5122,0.5215,0.5309,0.5406,0.5492,0.5587])

pic=plt.figure(figsize=(8,6),dpi=80)

plt.scatter(t,R,c='k',s=25,marker='x')
plt.xlim(10,70)
plt.ylim(0.45,0.56)
plt.yticks(np.arange(0.45,0.57,0.01))
plt.xlabel('Temperature (℃)')
plt.ylabel('Electric Resistance (mΩ)')

line=LinearRegression()
line.fit(t,R)
alpha=line.intercept_[0] #截距
beta=line.coef_[0][0]   #斜率
x=np.linspace(10,70,3)
y=alpha+beta*x

print('斜率：', beta)
print('截距: ', alpha)

x_test=t
y_pre=alpha+beta*x_test
y_real=R
print('线性回归模型的R^2=' , r2_score(y_pre,y_real))
plt.plot(x,y,'k-')

line.score(t,R)

plt.savefig('d:\python\Python_workspace\physics\\figure1.png')
plt.show()