# Cria vetor com amostras de uma senoide

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

# cria vetor t com t = 0 a 1 e passo dt = 0,01
dt = 0.01
t = arange(0,1,dt)

# cria amostras senoidais nos pontos do vetor t com freqeuncia f
A = 0.1
f = 5
s = A*sin(2*pi*f*t) 

# saida grafica
plot(t,s)
plt.plot(t,s)
plt.show()

fim()


