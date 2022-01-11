import numpy as np
import pandas as pd

x = np.array([14.5,77.61,191.0,353.3,567.2], dtype='float')
T = np.array([1.825,2.323,3.019,3.790,4.625])

I = 573000*T*T/(4*3.14*3.14)


print(I)

