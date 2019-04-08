# Programa para limiarizar a imagem pelo metodo de Pun
# O metodo de Pun calcula o limiar otimo pelo maximo da entropia
# a posteriori total das classes
#

import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from pylab import *
from sys import exit as fim

# le imagem de arquivo
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 
M = Image.open(arq)
width , height = M.size
N = width * height

# Obtem o histograma de frequencias relativas
h = M.histogram()
h = [m/float(N) for m in h]

# calcula entropia H baseada no histograma h da imagem original
H = np.sum([-1.0*np.log2(m)*m for m in h if m > 0])
print "entropia imagem= ", H

# ----------------------------------------------------------------
# determinacao do limiar L pelo metodo de Pun
# maximizacao por varredura completa do intervalo 0 a 255 (forca bruta)
L = 0
Hmax = 0
for k in range(255):
    HA = 0
    HB = 0
    for kA in range(k+1):
        m = h[kA]
        if m > 0 :
            HA = HA - np.log2(m)*m
    for kB in range(k+1,256):
        m = h[kB]
        if m > 0 :
            HB = HB - np.log2(m)*m
    HT = HA + HB
    if HT > Hmax:
        Hmax = HT
        L = k
        
#------------------------------------------------------------------
# IB imagem binarizada - valores 0 e 255
# M imagem original
IB = Image.new('L', [width,height])
print "limiar automatico = ", L
for i in range (width):
    for j in range (height):
        v = M.getpixel((i,j))
        if v <= L :
            IB.putpixel((i,j),0)
        else:
            IB.putpixel((i,j),255)
            
IB.show()

#------------------------------------------------------------------
# exibe as particoes do histograma
# Obs - para usar  fill_between() precisa transformar
#       as listas em arrays (do numpy)
#

# cria array da variavel independente = tons de cinza
x = np.arange(0,256,1)

# cria array para h = histograma
y1 = np.array(h)

# fill_between preenche entre y1 e y2
#     aqui y2 = 0 (eixo x)
y2 = 0

# cria figura para mostrar as particoes
fig = figure()
ax = fig.add_subplot(111)
ax.plot(x, h, color='blue')
ax.fill_between(x, y1, y2, where=x<L, facecolor='black')
ax.fill_between(x, y1, y2, where=x>=L, facecolor='red')
ax.set_title('Limiarizacao - Metodo de Pun')
show()


fim()
