# -*- coding: latin-1 -*-
#
# Programa problema17a.py

# Programa que lê uma seqüência de n números inteiros e
# a imprime, eliminando as repetições

# Versão 17a: solução na qual toda a seqüência é inicialmente
# lida e armazenada numa lista e em seguida percorrida imprimindo-se
# os números que não são repetições


def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return


    seq = []   # cria uma lista vazia


    # leitura da seqüência
    i=0
    while i<n:
        num = input("Num: ")
        seq = seq + [num]
        i = i+1



    # Impressão, eliminando-se as repetições.
    # Para cada elemento da seq., verifica se
    # esse elemento apareceu antes na seq. 

    i=0
    while i<n :

        j = 0
        achou = 0
        while j<=i-1 and achou==0:
            if seq[i] == seq[j]:
                achou = 1
            j = j+1

        if achou == 0:
            print seq[i],

        i = i+1

    print
# FIM


main()
