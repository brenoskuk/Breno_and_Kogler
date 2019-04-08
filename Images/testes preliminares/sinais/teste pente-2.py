# cria a funcao pente para amostrar sinais com intervalo de amostragem 'ta'

from pylab import *
import numpy
from sinal import *

dt = 0.1
t = arange(0,1,dt)
print t

y = t**2
print y

a = 3
ta = a*dt   

ya = y * Pente(t,ta)
print ya


