# Cria vetor com amostras de senoide ruidosa

from string import split
from pylab import *
import Image
import numpy
import matplotlib.pyplot as plt

# cria vetor t com t=0 a 10 e passo dt = 0,01
dt = 0.01
t = arange(0,10,dt)

# gera vetor de ruido aleatorio com o tamanho de t 
nse = randn(len(t))

# gera vetor exponencial calculado nos pontos de t
r = exp(-t/0.05)

# gera vetor de ruido filtrado por convolucao de nse com r 
cnse = numpy.convolve(nse , r, mode='full')*dt
cnse = cnse[:len(t)]

#gera senoide ruidosa adicionando o vetor cnse aos potos da senoide
s = 0.1*sin(2*pi*t) + cnse

# monta graficos da senoide ruidosa e do espectro de potencias psd
subplot(211)
plot(t,s)
subplot(212)
psd(s,512, 1/dt)
plt.plot(t,s)
plt.show()



