# -*- coding: latin-1 -*-
#
# Programa bubble_sort.py

# Programa que l� uma seq��ncia de n�meros inteiros e
# a imprime, em ordem crescente. A seq��ncia � ordenada
# usando-se um algoritmo conhecido por bubble sort
# (ou ordena��o por bolhas)

#-------------------------------------------------------------
# OBSERVA��O: veja selection_sort.py antes
#-------------------------------------------------------------

# Id�ia do algoritmo:
# Repete-se um processo de forma que, ap�s a rodada
# de n�mero r, garante-se que todos os n�meros armazenados
# na lista das posi��es de �ndice n-1 a n-r (os �ltimos r
# elementos da lista) est�o ordenados e s�o
# os r maiores n�meros de toda a seq��ncia.
# (observe que as rodadas come�am em 1)
#
# Na rodada r, objetos adjacentes na lista, das posi��es
# 0 a n-r s�o comparados dois a dois e sempre que o
# elemento � esquerda for maior, os dois trocam de posi��o
# Com isso, o maior elemento � sucessivamente deslocado
# para a direita na lista.


# Fun��o bubble_sort()
# Par�metros:
#     x (entrada/sa�da) : uma lista de inteiros (poderia ser de n�meros reais
#                         ou de letras)
# Valor de retorno: nenhum
def bubble_sort(x):

    # calcula o tamanho da lista de entrada
    n = len(x)

    r = 1
    while r < n :

        # j para acessar essas posi��es posteriores a i
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

    # leitura da seq��ncia
    entrada = raw_input("Digite uma sequencia de numeros separados por espaco e termine com ENTER\n")

    seq = []   # cria uma lista vazia

    # convertemos os elementos da string entrada
    # para n�mero e concatenamos � lista seq.
    for elemento in entrada.split():
        seq = seq + [int(elemento)]  


    # Ordena��o

    bubble_sort(seq)


    # Impress�o da lista ordenada
    for i in range(len(seq)):
        print seq[i],

    print


# FIM


main()
