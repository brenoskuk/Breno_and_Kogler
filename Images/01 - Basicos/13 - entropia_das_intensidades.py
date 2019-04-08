# Programa para calcular a entropia de tons de cinza de uma imagem
#

import Image
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim


# le imagem de arquivo
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 
M = Image.open(arq)
width , height = M.size
N = width * height

# obtem o histograma h de frequencias absolutas
h = M.histogram()
h = [m/float(N) for m in h]

# calcula a entropia H (em bits - usa log base 2 )
#  a partir do histograma h da imagem
H = numpy.sum([-1.0*numpy.log2(m)*m for m in h if m > 0])
print "entropia = ", H

# exibe a imagem
M.show()

# mostra o histograma (opcional)
#plt.plot(h)
#plt.show()
#fim()
