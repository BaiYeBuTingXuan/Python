import numpy as np

def stderror( a ):
    return np.sqrt(((a - np.mean(a)) ** 2).sum() / ((a.size - 1)*a.size))

M0=np.array([84.1177,84.1120,84.1113,84.1125,84.1121])
M1=np.array([84.3177,84.3171,84.3166,84.3160,84.3128])

averM0=M0.mean()
averM1=M1.mean()

print("M0 =",averM0)
print("M1 =",averM1)

M=averM1-averM0
print("M =",M)

M0_e = stderror(M0)
M1_e = stderror(M1)

print("M0 error =",M0_e)
print("M1 errpr =",M1_e)