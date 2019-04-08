# Cria vetor com amostras e calcula a transformada rapida de Fourier (fft)

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim


# ---------------- DADOS DA ANALISE
#
# cria vetor t com pontos espacados de dt, indo de t0 a t_max
dt = 0.001
t0 = 0
t_max = 1
t = arange(t0,t_max,dt)

# intervalo de amostragem ta
#  (nesta simulacao, ta e' multiplo de dt, sendo 'a' a multiplicidade)
a = 2
ta = a*dt

# funcao f(t) que descreve o
f = 1*sin(2*pi*5*t) + 0.5*sin(2*pi*10*t)+ 0.25*sin(2*pi*20*t)


# ---------------- Cálculo dos parâmetros da análise
#
# largura TJ da janela e a resolucao de frequencia de analise w0
TJ = t_max - t0
w0 = (2*pi)/TJ
print 'duracao do sinal TJ = ',TJ
print 'resolucao da frequencia w0 = ',w0

# frequencia de amostragem correspondente a ta
wa = (2*pi)/ta
print 'periodo de amostragem ta = ta'
print 'frequencia de amostragem wa = ',wa

# quantidade total de amostras N
# quantidade maxima de harmonicas M
N = floor(TJ/ta)
M = floor(N/2)
print 'quantidade de amostras N = ',N
print 'quantidade de harmonicas M = ',M

# funcao pente para realizar amostragem
pente = t-t
for i in range(len(t)):
    chave = mod(i,a)
    if chave == 0:
        pente[i] = 1 

# cria amostras da funcao f(t) para os pontos do vetor t
fa = f * pente

# transformada de Fourier F(w) da funcao f
F = fft(fa, n=None, axis=0)
Fs = fftshift(F, axes=None)
w = range(-len(t)/2 , len(t)/2)

# monta os graficos das amostras de f e do espectro TF
subplot(211)
plot(t,f,'r-',t,fa,'bo')
grid(True)
xlabel('x')
ylabel('I(x)')

subplot(212)
grid(True)
xlabel('frequencia')
ylabel('amplitude')
min_x = w[0]
max_x = w[len(w)-1]
y = absolute(Fs)
max_y = max(y)
min_y = 0
markerline, stemlines, baseline = stem(w, y, 'r-', 'r,')
setp(markerline, 'markerfacecolor', 'r','linewidth', 6)
setp(baseline, 'color','r', 'linewidth', 2)
plt.axis([min_x,max_x,min_y,max_y])
plt.show()

fim()

