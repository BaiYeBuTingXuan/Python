import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score

m1 = 188.2
m2 = 336.8

v10 = np.array([65.79,81.54,63.31,74.04,74.42,59.76],dtype='float')
v20 = np.array([-51.78,-51.53,-44.40,-57.01,-48.49,-39.10],dtype='float')
v11 = np.array([-17.92,-13.93,-16.27,-18.05,-17.03,-15.06],dtype='float')
v21 = np.array([83.22,110.95,89.96,102.08,99.83,78.84],dtype='float')



p1 = m2*v10+m1*v20
p2 = m2*v11+m1*v21

E1 = (m2*(v10*v10)+m1*(v20*v20))/2
E2 = (m2*(v11*v11)+m1*(v21*v21))/2

delta_p = p1 - p2
delta_E = E1 - E2

print(p1)
print(p2)
print(E1)
print(E2)
print(delta_p)
print(delta_E)

data = pd.DataFrame([v10,v20,v11,v21,p1,p2,E1,E2,delta_p,delta_E],index=['v10','v20','v11','v21','p1','p2','E1','E2','delta_p','delta_E'])

print(data)

data.to_excel(excel_writer='d:\python\Python_workspace\physics\\excel8.xlsx') 
#和to_csv不同,to_excel需要预先有文件 也就是默认'r'模式而非'w'模式