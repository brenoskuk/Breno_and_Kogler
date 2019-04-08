# Le arquivo contendo o nucleo de convolucao
# e executa a convolucao sobre uma imagem dada

from string import split
import Image
import numpy
import matplotlib.pyplot as plt

# ----------- Le imagem
I = Image.open('.\Lena.png')
width , height = I.size
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"

# ----------- Le arquivo do nucleo de convolucao
# primeiro le tamanho do nucleo
N = input("Entre a ordem do nucleo N x N com N impar: ")
L = (N-1)/2
# leitura do nome do arquivo do nucleo
nome_arq = raw_input("Digite o arquivo a ser lido :")
if len(nome_arq)==0:
    nome_arq = "nucleo.txt"
# abre arquivo para leitura
f = open(nome_arq, 'r')
#move o ponteiro para o inicio do arquivo
f.seek(0)

# ------------ Transfere o nucleo lido para matriz G(i,j) de convolucao
G = []
for line in f:
    vals=line.split()
    Lin = []
    for j in range(N):
        Lin = Lin + [int(vals[j])]
    G = G + [Lin]
    
#imprime o nucleo de convolucao G(i,j)
for m in range(N):
    for n in range(N):
        print G[m][n],
    print

Soma = 0
for m in range(N):
    for n in range(N):
        Soma = Soma + G[m][n]
A = 1/float(Soma)
print A

# ------------- Cria matrizes M e F
W = width
H = height
M = []
F = []
for i in range(W) :
    Lin = []
    for j in range(H):
        Lin = Lin + [0]
    M = M + [Lin]
for i in range(W) :
    Lin = []
    for j in range(H):
        Lin = Lin + [0]
    F = F + [Lin]

# ------------- Copia imagem na matriz M  e inicializa a matriz F  
for i in range (W):
    for j in range (H):
        M[i][j] = I.getpixel((i,j))

for i in range (W):
    for j in range (H):
        F[i][j] = 0
       
# ------------- Realiza convolucao
T = Image.new('L', [W,H])
for i in range (N,W-N):
    for j in range (N,H-N):
        Soma = 0
        for m in range(N):
            for n in range(N):   
                Soma = Soma + G[m][n]*M[i+m-L][j+n-L]
        F[i][j]= Soma * A 
        T.putpixel((i,j),F[i][j])
        
T.show()
