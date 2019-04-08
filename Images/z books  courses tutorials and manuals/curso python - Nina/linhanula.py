# Programa que verifica se uma matriz possui uma linha
# so' com zeros.

from string import split
from matriz import *


# Programa principal
def main():
    print "Digite o numero de linhas e colunas da matriz, separado por espaco: "
    entrada = raw_input()

    # separar m de n e colocar nas respectivas variaveis
    x = entrada.split()
    m,n = int(x[0]),int(x[1])
    
    # ou 
    # m,n = map(int, entrada.split())



    print "Digite uma matriz %d x %d, linha a linha" %(m,n)

    M = LeMatriz(m,n)



    # procura uma linha so' com zeros
    achou = 0
    i = 0
    while i<m and achou==0:

        sozeros = 1
        j = 0
        while j<n and sozeros==1:
            if M[i][j] != 0:
                sozeros = 0
            j = j + 1

        if sozeros==1:
            achou=1

        i = i + 1




    # imprime a resposta
    print "A matriz "    
    ImprimeMatriz(M)

    if achou==1:
        print "possui uma linha so' com zeros"
    else:
        print "nao possui uma linha so' com zeros"
