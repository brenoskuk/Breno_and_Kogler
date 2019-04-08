# cria a funcao pente para amostrar sinais com intervalo de amostragem 'ta'

from pylab import *
import numpy

dt = 0.1
t = arange(0,1,dt)
print t

y = t**2
print y

pente = t-t
print pente

a = 3
ta = a*dt
for i in range(len(t)):
    chave = mod(i,a)
    if chave == 0:
        pente[i] = 1 
print pente    

ya = y * pente
print ya


