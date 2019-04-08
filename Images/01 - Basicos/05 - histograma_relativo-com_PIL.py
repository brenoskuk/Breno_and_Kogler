# imprime e plota os valores do histograma de frequencias relativas

import Image
import numpy
import matplotlib.pyplot as plt
from sys import exit as fim

# le imagem de um arquivo
M = Image.open('.\Lena.png')
width , height = M.size
N = width * height

# calcula o histograma absoluto usando a funcao do PIL
h = M.histogram()

# obtem histograma de frequencias relativas
#  dividindo-se as frequencias absolutas em h por N = 
#  = quantidade total de pixels na imagem
h = [m/float(N) for m in h]

# imprime e mostra o histograma relativo
for k in range(256):
    print h[k]
plt.plot(h)
plt.show()

# fim() = sys.exit --- evita que ao usar o matplotlib haja
#   persistencia de um processo zumbi 
fim()
