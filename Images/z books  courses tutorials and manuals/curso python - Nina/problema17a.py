# -*- coding: latin-1 -*-
#
# Programa problema17a.py

# Programa que l� uma seq��ncia de n n�meros inteiros e
# a imprime, eliminando as repeti��es

# Vers�o 17a: solu��o na qual toda a seq��ncia � inicialmente
# lida e armazenada numa lista e em seguida percorrida imprimindo-se
# os n�meros que n�o s�o repeti��es


def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return


    seq = []   # cria uma lista vazia


    # leitura da seq��ncia
    i=0
    while i<n:
        num = input("Num: ")
        seq = seq + [num]
        i = i+1



    # Impress�o, eliminando-se as repeti��es.
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
