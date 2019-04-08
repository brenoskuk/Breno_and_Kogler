# Cria vetor com amostras de uma linha de uma imagem

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
import Image
from sys import exit as fim

# ----------- Le imagem
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 

I = Image.open(arq)
width , height = I.size
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"
W = width
H = height

# ------------- Seleciona coluna 
j = int(H/2)
print("Coluna default - cenral : "),j
# ------------- Cria vetor V com pontos da imagem
V = []
for m in range (W):
    V.append(0)
for i in range(W) :
    V[i] = I.getpixel((j,i))    


# saida grafica
plt.plot(V)
plt.show()

fim()

