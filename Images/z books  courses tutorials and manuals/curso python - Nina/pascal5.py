# -*- coding: latin-1 -*-
#
# Programa pascal5.py
# Versão 5: sem calcular fatorial, usando duas listas

# Lembre-se que o índice de uma lista em Python começa
# em 0. Logo, se a lista contém 10 elementos, os índices
# válidos variam de 0 a 9

def main():
    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    # cria a primeira linha (linha 0) e imprime
    # uma lista com 1 elemento (o número 1)
    atual = [1]

    print atual[0]

    # as próximas linhas, de 1 a n, são calculadas a partir da anterior
    for i in range(1,n+1):

        # aloca lista com i+1 elementos para armazenar os números da próxima linha
        # Do jeito que será feito, será alocada uma lista com os numeros de 1 a i+1
        # Na verdade, poderiam sem quaisquer números, desde que o
        # primeiro seja 1
        proxima = range(1,i+2)

        # o último elemento de uma linha é sempre 1
        # Lembre-se que a linha i contém i+1 elementos e
        # o (i+1)-ésimo elemento de uma lista encontra-se na
        # posição de índice i na lista
        proxima[i] = 1

        # calcular os números da linha, exceto o primeiro e o último
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
