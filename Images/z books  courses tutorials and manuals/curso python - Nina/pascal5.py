# -*- coding: latin-1 -*-
#
# Programa pascal5.py
# Vers�o 5: sem calcular fatorial, usando duas listas

# Lembre-se que o �ndice de uma lista em Python come�a
# em 0. Logo, se a lista cont�m 10 elementos, os �ndices
# v�lidos variam de 0 a 9

def main():
    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    # cria a primeira linha (linha 0) e imprime
    # uma lista com 1 elemento (o n�mero 1)
    atual = [1]

    print atual[0]

    # as pr�ximas linhas, de 1 a n, s�o calculadas a partir da anterior
    for i in range(1,n+1):

        # aloca lista com i+1 elementos para armazenar os n�meros da pr�xima linha
        # Do jeito que ser� feito, ser� alocada uma lista com os numeros de 1 a i+1
        # Na verdade, poderiam sem quaisquer n�meros, desde que o
        # primeiro seja 1
        proxima = range(1,i+2)

        # o �ltimo elemento de uma linha � sempre 1
        # Lembre-se que a linha i cont�m i+1 elementos e
        # o (i+1)-�simo elemento de uma lista encontra-se na
        # posi��o de �ndice i na lista
        proxima[i] = 1

        # calcular os n�meros da linha, exceto o primeiro e o �ltimo
        for j in range(1,i):
            proxima[j]=atual[j-1]+atual[j]


        # imprimir a linha i
        for j in range(0,i+1):
            print proxima[j],
        print


        # atualizar a atual, para que a proxima linha seja calculada
        # a partir da linha correta
        atual = proxima


# FIM
