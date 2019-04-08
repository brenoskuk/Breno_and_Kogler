# -*- coding: latin-1 -*-
#
# Programa problema15b.py

# Programa que l� uma seq��ncia de n n�meros inteiros e
# a imprime em ordem reversa.

# Vers�o 15b: A lista (vetor) com a sequ��ncia lida � constru�da
# gradativamente, concatenando-se cada elemento lido ao final da
# lista em constru��o
# Isso pode ser facilmente feito em Python, mas n�o necessariamente
# em outras linguagens
 
def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    seq = []   # cria uma lista vazia

    # leitura da seq��ncia
    i=0
    while i<n:
       num = input("Proximo: ")
       seq = seq + [num]          # este + n�o � opera��o de adi��o; � concatena��o de listas
       i = i+1

    # impress�o em ordem reversa
    i=n-1
    while i>=0 :
        print seq[i],
        i = i-1


# FIM


main()
