# cria a funcao pente para amostrar sinais com intervalo de amostragem 'ta'

from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

dx = 0.01
x = arange(0,1,dx)

# funcao f(x) que descreve o sinal
f = 1*sin(2*pi*1*x) + 0.5*sin(2*pi*2*x)+ 0.25*sin(2*pi*4*x)

# ----------------- AMOSTRAGEM
#

# intervalo de amostragem ta
#  (nesta simulacao, ta e' multiplo de dt, sendo 'a' a multiplicidade)
a = 5
ta = a*dx

# funcao pente para realizar amostragem
pente = x-x
for i in range(len(x)):
    chave = mod(i,a)
    if chave == 0:
        pente[i] = 1     

# cria amostras da funcao f(t) para os pontos do vetor t
fa = f * pente



# ------------------ Exibicao grafica dos resultados
#
# graficos  de f e  de fa (amostras de f)
subplot(211)
plot(x,f,'r-',x,fa,'bo')
grid(True)
xlabel('x')
ylabel('I(x)')

# grafico do pente(t)
subplot(212)
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
