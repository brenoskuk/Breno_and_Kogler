# Cria vetor com amostras de senoide e calcula densidade espectral de potencia

from string import split
from pylab import *
import Image
import numpy
import matplotlib.pyplot as plt

# cria vetor t para t=0 a 10 espacadas de dt=0,01
dt = 0.01
t = arange(0,10,dt)

# cria amostras da senoide para os pontos do vetor t
s = 0.1*sin(2*pi*t) 

# monta os graficos das amostras (senoide) e do espectro de potencias (psd)
subplot(211)
plot(t,s)
subplot(212)
psd(s,512, 1/dt)
plt.plot(t,s)
plt.show()



