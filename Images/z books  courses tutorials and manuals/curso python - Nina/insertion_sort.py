# -*- coding: latin-1 -*-
#
# Programa insertion_sort.py

# Programa que lê uma seqüência de números inteiros e
# a imprime, em ordem crescente. A seqüência é ordenada
# usando-se um algoritmo conhecido por insertion sort
# (ou ordenação por inserção)

#-------------------------------------------------------------
# OBSERVAÇÃO: veja selection_sort.py antes
#-------------------------------------------------------------

# Função insertion_sort()
# Parâmetros:
#     x (entrada/saída) : uma lista de inteiros (poderia ser de números reais
#                         ou de letras)
# Valor de retorno: nenhum
def insertion_sort(x):

    # calcula o tamanho da lista de entrada
    n = len(x)

    i = 1
    while i < n :

        j = i - 1
        aux = x[i]
        while j >= 0 and x[j]>aux :
            x[j+1] = x[j]
            j=j-1

        x[j+1] = aux

        i = i+1



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

    insertion_sort(seq)


    # Impressão da lista ordenada
    for i in range(len(seq)):
        print seq[i],

    print


# FIM


main()
