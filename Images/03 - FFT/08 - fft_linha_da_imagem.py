# Cria vetor com amostras de uma linha de uma imagem

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
import Image
from sys import exit as fim

# ----------- Le imagem
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 

I = Image.open(arq)
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


# ------------- ANALISE DE FOURIER
#
# transformada de Fourier (TF) das amostras no vetor V
TF = fft(V, n=None, axis=0)
TFs = fftshift(TF, axes=None)
w = range(-len(V)/2 , len(V)/2)


# monta os graficos das amostras de f e do espectro TF
subplot(211)
plot(V)
grid(True)
xlabel('x')
ylabel('I(x)')

subplot(212)
#bar(NFs, TFs)
grid(True)
xlabel('numero de onda')
ylabel('amplitude')
#plt.bar(NFs,TFs)
min_x = w[0]
max_x = w[len(w)-1]
y = absolute(TFs)
max_y = max(y)
min_y = 0
markerline, stemlines, baseline = stem(w, y, 'r-', 'r,')
setp(markerline, 'markerfacecolor', 'r','linewidth', 6)
setp(baseline, 'color','r', 'linewidth', 2)
plt.axis([min_x,max_x,min_y,max_y])

plt.show()

fim()
