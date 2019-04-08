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

# -------------  arranja 2 imagens na mesma linha
# subplot(LCN)
# L = quantidade de linhas
# C = quantidade de colunas
# N = numero sequencial do subplot

subplot(121)
im = plt.imshow(M1, cmap=cm.gray, origin='lower')
title('sem ruido')

subplot(122)
im = plt.imshow(M2, cmap=cm.gray, origin='lower')
title('ruido gaussiano')

plt.show()

fim()

