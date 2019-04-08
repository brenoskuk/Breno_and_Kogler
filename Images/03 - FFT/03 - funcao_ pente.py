# cria a funcao pente para amostrar sinais com intervalo de amostragem 'ta'

from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

dx = 0.01
x = arange(0,1,dx)

pente = x-x

a = 10
ta = a*dx
for i in range(len(x)):
    chave = mod(i,a)
    if chave == 0:
        pente[i] = 1     


# grafico do pente(t)
grid(True)
xlabel('x')
ylabel('pente(x)')
min_x = 0
max_x = 1
max_y = 2
min_y = 0
markerline, stemlines, baseline = stem(x, pente, 'r-', 'ro')
setp(markerline, 'markerfacecolor', 'r','linewidth', 2)
setp(baseline, 'color','r', 'linewidth', 1)
plt.axis([min_x,max_x,min_y,max_y])
plt.show()

fim()
