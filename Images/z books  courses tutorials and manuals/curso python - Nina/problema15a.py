# -*- coding: latin-1 -*-
#
# Programa problema15a.py

# Programa que lê uma seqüência de n números inteiros e
# a imprime em ordem reversa.

# Versão 15a: solução tradicional na qual uma lista
# (vetor) para armazenar a seqüência toda é pré-alocada
# antes do início da leitura da seqüência
 
def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    seq = n*[0]   # cria uma lista de tamanho n, preenchida com zeros

    # leitura da seqüência
    i=0
    while i<n:
       seq[i] = input("Proximo: ")
       i = i+1

    # impressão em ordem reversa
    i=n-1
    while i>=0 :
        print seq[i],
        i = i-1


# FIM


main()
