import numpy as np
import matplotlib.pyplot as plt
from numpy import poly1d
from numpy.core.function_base import linspace

coeff = np.array([-5.10784079e-09,3.21400926e-06,-8.81261585e-04,1.37505313e-01,-1.33517452e+01,8.26030987e+02,-3.17936605e+04,6.96003038e+05,-6.63426939e+06],dtype ='float')

f = poly1d(coeff)
f_ = np.polyder(f,1)

x = linspace(65,70,100)
coeff_ = np.roots(f_)
print(coeff_)
plt.xlim(67,68)
plt.ylim(-0.0001,0.0001)

plt.plot(x,f_(x))
plt.show()
