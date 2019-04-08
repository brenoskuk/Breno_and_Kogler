# Cria vetor com amostras de uma senoide

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

# cria vetor t com t = 0 a 1 e passo dt = 0,01
dt = 0.01
t = arange(0,1,dt)

# cria amostras composta por varias componentes senoidais nos pontos do vetor t 
A1 = 0.1
f1 = 2
A2 = 0.5
f2 = 5
s = A1*sin(2*pi*f1*t) + A2*sin(2*pi*f2*t)

# saida grafica
plot(t,s)
plt.plot(t,s)
plt.show()

fim()

