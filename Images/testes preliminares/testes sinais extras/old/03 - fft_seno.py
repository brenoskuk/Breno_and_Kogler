# Cria vetor com amostras e calcula a transformada rapida de Fourier (fft)

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

# cria vetor t para amostras espacadas de dt
dt = 0.001
t = arange(0,1,dt)

# cria amostras da funcao f para os pontos do vetor t
f = 1*sin(2*pi*64*t)

# calcula a transformada de Fourier (TF) da funcao f
TF = fft(f, n=None, axis=0)

# reformata o vetor de pontos da TF (shift) para exibicao
TFs = fftshift(TF, axes=None)

# monta o vetor de indices para o eixo da TF no grafico
NFs = range(-len(t)/2 , len(t)/2)

# monta os graficos das amostras de f e da TF
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
plt.axis([-100,100,-10,500])
plt.show()

fim()

