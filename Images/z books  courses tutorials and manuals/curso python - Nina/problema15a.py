# -*- coding: latin-1 -*-
#
# Programa problema15a.py

# Programa que l� uma seq��ncia de n n�meros inteiros e
# a imprime em ordem reversa.

# Vers�o 15a: solu��o tradicional na qual uma lista
# (vetor) para armazenar a seq��ncia toda � pr�-alocada
# antes do in�cio da leitura da seq��ncia
 
def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    seq = n*[0]   # cria uma lista de tamanho n, preenchida com zeros

    # leitura da seq��ncia
    i=0
    while i<n:
       seq[i] = input("Proximo: ")
       i = i+1

    # impress�o em ordem reversa
    i=n-1
    while i>=0 :
        print seq[i],
        i = i-1


# FIM


main()
