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
    


# ------------- ANALISE DE FOURIER
#
# transformada de Fourier (TF) das amostras da imagem I
TF = fft2(I, s=None, axes=(-2,-1))
#TFs = fftshift(TF, axes=None)
w = range(-(W)/2 , (W)/2)
TFw, TFh = shape(TF)

# monta os graficos das amostras de f e do espectro TF
subplot(211)
xlabel('x')
ylabel('I(x)')
im = plt.imshow(I, cmap=cm.gray, origin='lower')


subplot(212)
grid(True)
xlabel('x')
ylabel('I(x)')

S=[]
for i in range(TFw):
    Lin = []
    for j in range(TFh):
        Lin = Lin + [0]
    S = S + [Lin]
    
for i in range(TFw):
    for j in range(TFh):
        S[i][j] = (absolute(TF[i][j]))
        #S[i][j] = log1p(absolute(TF[i][j]))
print S[0][0]

xlabel('numero de onda')
ylabel('amplitude')
im = plt.imshow(S, origin='lower')
#im = plt.imshow(S, cmap=cm.gray, origin='lower')

#min_x = w[0]
#max_x = w[len(w)-1]
#y = absolute(TFs)
#max_y = max(y)
#min_y = 0
#markerline, stemlines, baseline = stem(w, y, 'r-', 'r,')
#setp(markerline, 'markerfacecolor', 'r','linewidth', 6)
#setp(baseline, 'color','r', 'linewidth', 2)
#plt.axis([min_x,max_x,min_y,max_y])

plt.show()

fim()
