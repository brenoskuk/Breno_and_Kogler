# Programa que verifica se uma matriz quadrada e' magica

from string import split
from matriz import *


# Programa principal
def main():

    print "Digite a dimensao da matriz (quadrada): "
    n = input()


    print "Digite uma matriz %d x %d, linha a linha" %(n,n)
    M = LeMatriz(n,n)


    # Calcula a soma da primeira linha; as demais serao comparadas com esta
    soma = 0
    for j in range(n):
        soma = soma + M[0][j]


    # variavel bandeirinha, para indicar se ainda há chance de ser magica
    igual = 1


    # verifica se a soma de cada linha e' igual a soma
    i = 1
    while i<n and igual==1:
        s=0
        for j in range(n):
            s = s + M[i][j]

        if s != soma:
            igual = 0

        i = i+1


    # verifica se a soma de cada coluna e' igual a soma
    j = 0
    while j<n and igual==1:
        s = 0
        for i in range(n):
            s = s + M[i][j]
        if s!=soma:
            igual = 0
        j = j+1



    # verifica se soma da diagonal principal e' igual a soma
    if igual==1:
        s = 0
        for i in range(n):
            s = s + M[i][i]
        if s!=soma:
            igual = 0


    # verifica se a soma da diagonal secundaria e' igual a soma
    if igual == 1:
        s = 0
        for i in range(n):
            s = s + M[i][n-i-1]
        if s != soma:
            igual = 0



    # imprime resposta
    if igual==1:
        print "A matriz e' magica"
    else :
        print "A matriz nao e' magica"


# FIM
