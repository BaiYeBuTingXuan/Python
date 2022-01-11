import numpy as np
import pandas as pd

a = np.array([685.4,687.2,679.2,683,1,681.1,680.0,677.4,683.5],dtype='float')



b = a.std()
c = np.mean(a)
d = a.sum()
print("b =",b)
print("c =",c)
print("d =",d)