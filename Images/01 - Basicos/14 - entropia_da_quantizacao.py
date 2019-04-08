# Programa para quantizar uniformemente as intensidades (original = 8 bits)
# de uma imagem reduzindo a quantidade de bits necessaria para n < 8 bits
#
import Image
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from sys import exit as fim

# le imagem de arquivo
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 
M = Image.open(arq)
width , height = M.size

# determina quantizacao
b = input("Entre um valor entre 1 e 8 bits: ")
d = 2.0**(8 - b)

# quantiza a imagem dada
Q = Image.new('L', [width,height])
for i in range (width):
    for j in range (height):
        v = M.getpixel((i,j))
        Q.putpixel((i,j),floor(v/d))

# obtem o histograma de frequencias relativas da imagem quantizada       
N = width * height
h = Q.histogram()
h = [m/float(N) for m in h]

# calcula a entropia dos pixels da imagem quantizada
H = np.sum([-1.0*np.log2(m)*m for m in h if m > 0])
print "entropia = ", H

Q.show()

# exibe o histograma usando o tipo stem (linhas verticais)
max_gray = floor(255/d)
max_freq = np.max(h)
v = range(256)
markerline, stemlines, baseline = stem(v, h, 'r-', 'r,')
setp(markerline, 'markerfacecolor', 'r','linewidth', 6)
setp(baseline, 'color','r', 'linewidth', 2)
plt.axis([-0.1,max_gray+0.1,0,max_freq])
plt.show()


fim()
