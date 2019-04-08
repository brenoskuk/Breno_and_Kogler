# Programa para ler uma imagem em uma matriz M e exibir a matriz
#

import Image
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from pylab import *
from sys import exit as fim

M1 = Image.open('.\geometrica.png')
print "tamanho = ", M1.size , "pixels"
print "tipo = ", M1.mode

M2 = Image.open('.\geometrica_ruido_gauss.png')
print "tamanho = ", M2.size , "pixels"
print "tipo = ", M2.mode

# -------------  arranja imagens e histogramas
# subplot(LCN)
# L = quantidade de linhas
# C = quantidade de colunas
# N = numero sequencial do subplot

subplot(221)
im = plt.imshow(M1, cmap=cm.gray, origin='lower')
title('sem ruido')

subplot(222)
im = plt.imshow(M2, cmap=cm.gray, origin='lower')
title('ruido gaussiano')

subplot(223)
h1 = M1.histogram()
plt.plot(h1)


subplot(224)
h2 = M2.histogram()
plt.plot(h2)

plt.show()

fim()

