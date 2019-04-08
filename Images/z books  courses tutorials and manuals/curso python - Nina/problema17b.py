# -*- coding: latin-1 -*-
#
# Programa problema17a.py

# Programa que lê uma seqüência de n números inteiros e
# a imprime, eliminando as repetições

# Versão 17a: solução na qual os elementos da seq. são lidos, mas
# apenas aqueles que não são repetição são armazenados. Em seguida
# os armazenados são impressos


def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return


    seq = []   # cria uma lista vazia


    # leitura da seqüência e armazenamento na lista, eliminando-se as repetições
    k = 0   # quantidade de números efetivamente armazenados
    i = 0   # quantidade de números lidos
    while i<n:
        num = input("Num: ")

        j = 0
        achou = 0
        while j<k and achou==0:
            if num == seq[j]:
                achou = 1
            j = j+1

        if achou == 0:
            seq = seq + [num]
            k = k + 1

        i = i+1



    # Impressão dos números armazenados

    for i in range(k):
        print seq[i],

    print

# FIM


main()
