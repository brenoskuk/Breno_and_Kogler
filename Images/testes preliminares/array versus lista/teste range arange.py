import matplotlib.mlab as mlab
from pylab import figure, show
import numpy as np

a=range(10)
print 'a= ',a

b=np.arange(10)
print 'b= ',b

v=[]
for i in range(10):
    v.append(i*i)
print 'v= ',v

u=np.array(v)
print 'u= ',u
