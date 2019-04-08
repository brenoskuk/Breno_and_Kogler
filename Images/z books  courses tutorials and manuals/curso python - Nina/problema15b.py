# -*- coding: latin-1 -*-
#
# Programa problema15b.py

# Programa que lê uma seqüência de n números inteiros e
# a imprime em ordem reversa.

# Versão 15b: A lista (vetor) com a sequüência lida é construída
# gradativamente, concatenando-se cada elemento lido ao final da
# lista em construção
# Isso pode ser facilmente feito em Python, mas não necessariamente
# em outras linguagens
 
def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    seq = []   # cria uma lista vazia

    # leitura da seqüência
    i=0
    while i<n:
       num = input("Proximo: ")
       seq = seq + [num]          # este + não é operação de adição; é concatenação de listas
       i = i+1

    # impressão em ordem reversa
    i=n-1
    while i>=0 :
        print seq[i],
        i = i-1


# FIM


main()
