# Programa para calcular e mostrar o histograma de uma imagem
# metodo eficiente - varre a imagem 1 so vez
#

import Image
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

# le uma imagem de um arquivo
M = Image.open('.\Lena.png')
width , height = M.size
N = width * height
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"
print "# pixels = largura x altura = " , N

# cria o vetor h[] para o histograma de frequencias absolutas
h = []
for m in range (255):
    h.append(0)
for i in range (width):
    for j in range (height):
         v = M.getpixel((i,j))
         h[v]= h[v] + 1
         
M.show()
plt.plot(h)
plt.show()

fim()
