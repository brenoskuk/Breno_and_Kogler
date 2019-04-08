# Cria vetor com amostras e calcula a transformada rapida de Fourier (fft)

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

# cria vetor t para amostras espacadas de dt
dt = 0.001
t = arange(0,1,dt)

# cria amostras da funca f para os pontos do vetor t
f = 1*sin(2*pi*5*t) + 0.5*sin(2*pi*10*t)+ 0.25*sin(2*pi*20*t)

# transformada de Fourier (TF) da funcao f
TF = fft(f, n=None, axis=0)
TFs = fftshift(TF, axes=None)
NFs = range(-len(t)/2 , len(t)/2)

# monta os graficos das amostras de f e do espectro TF
subplot(211)
plot(t,f)
grid(True)
xlabel('x')
ylabel('I(x)')

subplot(212)
bar(NFs, TFs)
grid(True)
xlabel('frequencia')
ylabel('amplitude')
plt.bar(NFs,TFs)
plt.axis([-50,50,-10,500])
plt.show()

fim()

