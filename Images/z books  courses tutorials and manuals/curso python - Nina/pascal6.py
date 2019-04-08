# -*- coding: latin-1 -*-
#
# Programa pascal6.py
# Vers�o6: sem calcular fatorial e usando APENAS uma lista

# Lembre-se que o �ndice de uma lista em Python come�a
# em 0. Logo, se a lista cont�m 10 elementos, os �ndices
# v�lidos variam de 0 a 9

def main():
    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return

    c = range(1,n+2)  # [1,2,3,...,n+1]

    print c[0]  # a primeira linha (linha 0) tem apenas um elemento

    i = 1
    while i<=n:

        # elemento na coluna i da linha i � 1 sempre
        # Lembre-se que a linha i cont�m i+1 elementos e
        # o (i+1)-�simo elemento de uma lista encontra-se na
        # posi��o de �ndice i na lista
        c[i]=1

        # a soma dois a dois para gerar a pr�xima linha
        # � realizada de tr�s para a frente, pois a 
        # pr�xima linha ser� armazenada na mesma lista.
        # Se fosse calculada da esquerda para a direita,
        # o valor j� modificado seria utilizado na adi��o,
        # resultando em soma maior que o correto.
        j=i-1
        while j>=1:
            c[j]=c[j-1]+c[j]
            j=j-1

        for j in range(0,i+1):
            print c[j],
        print

        i = i+1

# FIM

main()
