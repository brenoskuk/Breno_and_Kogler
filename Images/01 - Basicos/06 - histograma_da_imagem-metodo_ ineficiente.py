# Programa para calcular e mostrar o histograma de uma imagem
# metodo INEFICIENTE - varre a imagem 256 vezes
# contando as frequencias do valor no pixel em cada varredura
#

import Image
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim


# le image de um arquivo
M = Image.open('.\Lena.png')
width , height = M.size
N = width * height
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"
print "# pixels = largura x altura = " , N

# cria vetor h[] de tamanho 256 e o preenche com o histograma
h = []
for m in range(255):
    h.append(0)
for v in range(255):
    for i in range(width):
        for j in range(height):
            if v == M.getpixel((i,j)):
                h[v]= h[v] + 1 

            
M.show()
plt.plot(h)
plt.show()

fim()
