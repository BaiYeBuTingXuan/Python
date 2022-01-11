import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score

T = pd.DataFrame([26.2,32.2,37.5,41.5,46.7,48.7,55.2,61.4,66.4],dtype='float')
omiga = pd.DataFrame([56.85,58.12,59.25,60.07,61.16,61.56,63.15,64.30,65.40],dtype='float')

pic=plt.figure(figsize=(8,6),dpi=80)

plt.scatter(T,omiga,c='k',s=25,marker='x')
plt.xlim(20,70)
plt.ylim(56,66)
# plt.xticks(np.arange(24,88,16))
plt.xlabel('Temperature /$^\circ$C')
plt.ylabel('Electric Resistance /$\Omega$')

line=LinearRegression()
line.fit(T,omiga)
alpha=line.intercept_[0] #截距
beta=line.coef_[0][0]   #斜率
x=np.linspace(20,70,3)
y=alpha+beta*x

print('斜率：', beta)
print('截距: ', alpha)

x_test=T
y_pre=alpha+beta*x_test
y_real=omiga
print('线性回归模型的R^2=' , r2_score(y_pre,y_real))

plt.plot(x,y,'k--')

plt.title("FIGURE: Temperature - Resistence Charaterized Curve")
plt.savefig('d:\python\Python_workspace\physics\\figure10.png')
plt.show()

