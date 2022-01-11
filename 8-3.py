import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score

m1 = 329.7
m2 = 188.8

v10 = np.array([18.17,26.98,26.90,17.30,21.36,18.52],dtype='float')
v20 = np.array([-23.38,-22.98,-27.66,-20.40,-19.58,-16.76],dtype='float')
v = np.array([3.25,4.51,4.23,3.88,3.93,3.09],dtype='float')




p1 = m2*v10+m1*v20
p2 = -(m2+m1)*v

E1 = (m2*(v10*v10)+m1*(v20*v20))/2
E2 = ((m2+m1)*(v*v))/2

delta_p = p1 - p2
delta_E = E1 - E2

print(p1)
print(p2)
print(E1)
print(E2)
print(delta_p)
print(delta_E)

data = pd.DataFrame([v10,v20,v,p1,p2,E1,E2,delta_p,delta_E],index=['v10','v20','v','p1','p2','E1','E2','delta_p','delta_E'])

print(data)

data.to_csv('d:\python\Python_workspace\physics\\excel8-3.csv')