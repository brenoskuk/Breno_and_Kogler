# Programa para quantizar uniformemente as intensidades (original = 8 bits)
# de uma imagem reduzindo a quantidade de bits necessaria para n < 8 bits
#
import Image
import numpy
import matplotlib.pyplot as plt
from pylab import *
from sys import exit as fim

# le imagem de arquivo
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 
M = Image.open(arq)
width , height = M.size
N = width * height

# determina quantizacao
b = input("Entre um valor entre 1 e 8 bits: ")
d = 2.0**(8 - b)

# quantiza a imagem dada
Q = Image.new('L', [width,height])
for i in range (width):
    for j in range (height):
        v = M.getpixel((i,j))
        Q.putpixel((i,j),floor(v/d))

# mostra imagens e histogramas relativos
subplot(221)
im = plt.imshow(M, cmap=cm.gray, origin='lower')
title('original')

subplot(222)
max_gray = floor(255/d)
im = plt.imshow(Q, vmin=0, vmax=max_gray, cmap=cm.gray, origin='lower')
title('quantizada')

subplot(223)
h1 = M.histogram()
h1 = [m/float(N) for m in h1]
plt.plot(h1)


subplot(224)
h2 = Q.histogram()
h2 = [m/float(N) for m in h2]
plt.axis([0,max_gray,0,1])
plt.plot(h2)

plt.show()


fim()
