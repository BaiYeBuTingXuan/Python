import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

C = np.arange(0,8,1)
I = np.array([373.7,314.5,250.6,191.8,147.2,147.2,148.7,187.6])
I = I*(10**(-3))
U = np.array([224.7,224.8,224.7,224.7,225.0,224.8,225.2,225.5])
P = np.array([25.2,25.1,25.1,25.1,25.0,25.0,25.2,25.2])
cos = P/(U*I)

print(C)
print(I)
print(U)
print(P)
print(cos)

pic=plt.figure(figsize=(8,6),dpi=80)
plt.scatter(C,cos,s=20,marker='o',c = 'k',)
plt.plot(C,cos,'k--')
plt.xlim(-0.2,7.2)
plt.ylim(0.29,0.79)
plt.xticks(np.arange(0,8,1))
plt.yticks(np.arange(0.29,0.79,0.05))
plt.xlabel('Electric Capacity ({}F)'.format(chr(956)))
plt.ylabel('AC Power Factor cos{}'.format(chr(966)))

plt.savefig("d:\\python\\Python_workspace\\physics\\figure4.png")
plt.show()