import numpy as np
from numpy import poly1d,polyfit
import matplotlib.pyplot as plt
from numpy.testing._private.utils import print_assert_equal
import pandas as pd

pic=plt.figure(figsize=(8,6),dpi=80)

x = np.linspace(0,3,100)
plt.plot(x,np.sin(x))

coeff = polyfit(x,np.sin(x),1)
print(coeff)
f = poly1d(coeff)
plt.plot(x,f(x))


plt.show()