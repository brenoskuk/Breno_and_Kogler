# Cria vetor com amostras de uma linha de uma imagem

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
import Image
from sys import exit as fim

# ----------- Le imagem
I = Image.open('.\matches.png')
width , height = I.size
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"
W = width
H = height

# ------------- Seleciona linha l
j = int(H/2)

# ------------- Cria vetor V com pontos da imagem
V = []
for m in range (W):
    V.append(0)
for i in range(W) :
    V[i] = I.getpixel((i,j))    


# transformada de Fourier (TF) das amostras no vetor V
TF = fft(V, n=None, axis=0)
TFs = fftshift(TF, axes=None)
NFs = range(-len(V)/2 , len(V)/2)


# monta os graficos das amostras de f e do espectro TF
subplot(211)
plot(V)
grid(True)
xlabel('x')
ylabel('I(x)')

subplot(212)
bar(NFs, TFs)
grid(True)
xlabel('frequencia')
ylabel('amplitude')
plt.bar(NFs,TFs)
plt.show()

fim()
