import numpy as np 
import matplotlib.pyplot as plt
import random
def func(x):
    return 3*np.square((1-np.exp(-2*(x-0.5))))
x=np.linspace(0,5,1000)
y=func(x)
k=np.linspace(0,5,1000)
l=np.random.uniform(-0.5,0.5,1000)
#k_random=np.array([random.random() for i in l ])
z=func(k)+l
figax=plt.subplots(figsize=(10,7))
plt.plot(x,y,'b',linewidth=2)
plt.scatter(k,z,c='r',s=5)
