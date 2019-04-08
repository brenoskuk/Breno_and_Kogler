# -*- coding: latin-1 -*-
#
# Programa insertion_sort.py

# Programa que l� uma seq��ncia de n�meros inteiros e
# a imprime, em ordem crescente. A seq��ncia � ordenada
# usando-se um algoritmo conhecido por insertion sort
# (ou ordena��o por inser��o)

#-------------------------------------------------------------
# OBSERVA��O: veja selection_sort.py antes
#-------------------------------------------------------------

# Fun��o insertion_sort()
# Par�metros:
#     x (entrada/sa�da) : uma lista de inteiros (poderia ser de n�meros reais
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

    # leitura da seq��ncia
    entrada = raw_input("Digite uma sequencia de numeros separados por espaco e termine com ENTER\n")

    seq = []   # cria uma lista vazia

    # convertemos os elementos da string entrada
    # para n�mero e concatenamos � lista seq.
    for elemento in entrada.split():
        seq = seq + [int(elemento)]  


    # Ordena��o

    insertion_sort(seq)


    # Impress�o da lista ordenada
    for i in range(len(seq)):
        print seq[i],

    print


# FIM


main()
