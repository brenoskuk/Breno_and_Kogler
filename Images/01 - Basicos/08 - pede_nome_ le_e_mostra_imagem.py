# Programa para ler uma imagem em uma matriz M e exibir a matriz
#

import Image
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from pylab import *
from sys import exit as fim

nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 

M1 = Image.open(arq)
print "tamanho = ", M1.size , "pixels"
print "tipo = ", M1.mode

# outra forma de exibir uma imagem
# cmap escolhido = rampa de tons de cinza de 0 a 255 (cm.gray)
im = plt.imshow(M1, cmap=cm.gray, origin='lower')
plt.show()

fim()

