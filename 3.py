import numpy as np
import pandas as pd

def GetData(str):
    Data1 = pd.read_csv(str,sep=',',dtype='str')
    
    Data2 = pd.DataFrame(Data1.iloc[:,:],dtype='float')
    return Data2

a = GetData(r"d:\python\Python_workspace\physics\3.csv")
a.index=['U1','U2']

u1 = a.iloc[0,:]
u2 = a.iloc[1,:]

print(u1)
print(u2)

print(np.mean(u1))
print(np.mean(u2))

print(u1-5.04)