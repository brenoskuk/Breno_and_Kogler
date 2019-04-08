# -*- coding: latin-1 -*-
#
# Programa bubble_sort.py

# Programa que lê uma seqüência de números inteiros e
# a imprime, em ordem crescente. A seqüência é ordenada
# usando-se um algoritmo conhecido por bubble sort
# (ou ordenação por bolhas)

#-------------------------------------------------------------
# OBSERVAÇÃO: veja selection_sort.py antes
#-------------------------------------------------------------

# Idéia do algoritmo:
# Repete-se um processo de forma que, após a rodada
# de número r, garante-se que todos os números armazenados
# na lista das posições de índice n-1 a n-r (os últimos r
# elementos da lista) estão ordenados e são
# os r maiores números de toda a seqüência.
# (observe que as rodadas começam em 1)
#
# Na rodada r, objetos adjacentes na lista, das posições
# 0 a n-r são comparados dois a dois e sempre que o
# elemento à esquerda for maior, os dois trocam de posição
# Com isso, o maior elemento é sucessivamente deslocado
# para a direita na lista.


# Função bubble_sort()
# Parâmetros:
#     x (entrada/saída) : uma lista de inteiros (poderia ser de números reais
#                         ou de letras)
# Valor de retorno: nenhum
def bubble_sort(x):

    # calcula o tamanho da lista de entrada
    n = len(x)

    r = 1
    while r < n :

        # j para acessar essas posições posteriores a i
        j=0
        while j < n-r :
            if x[j] > x[j+1] :
                aux = x[j]
                x[j] = x[j+1]
                x[j+1] = aux
            j=j+1

        r=r+1



# Programa principal
def main():

    # leitura da seqüência
    entrada = raw_input("Digite uma sequencia de numeros separados por espaco e termine com ENTER\n")

    seq = []   # cria uma lista vazia

    # convertemos os elementos da string entrada
    # para número e concatenamos à lista seq.
    for elemento in entrada.split():
        seq = seq + [int(elemento)]  


    # Ordenação

    bubble_sort(seq)


    # Impressão da lista ordenada
    for i in range(len(seq)):
        print seq[i],

    print


# FIM


main()
