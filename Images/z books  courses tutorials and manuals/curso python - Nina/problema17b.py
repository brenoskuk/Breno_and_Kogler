# -*- coding: latin-1 -*-
#
# Programa problema17a.py

# Programa que l� uma seq��ncia de n n�meros inteiros e
# a imprime, eliminando as repeti��es

# Vers�o 17a: solu��o na qual os elementos da seq. s�o lidos, mas
# apenas aqueles que n�o s�o repeti��o s�o armazenados. Em seguida
# os armazenados s�o impressos


def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return


    seq = []   # cria uma lista vazia


    # leitura da seq��ncia e armazenamento na lista, eliminando-se as repeti��es
    k = 0   # quantidade de n�meros efetivamente armazenados
    i = 0   # quantidade de n�meros lidos
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



    # Impress�o dos n�meros armazenados

    for i in range(k):
        print seq[i],

    print

# FIM


main()
