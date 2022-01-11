import numpy as np
def diff(coeff):
    size = np.size(coeff)
    for i in np.arange(0,size,1):
        coeff[i] = coeff[i]*(size-i-1)
    return coeff