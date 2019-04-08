# -*- coding: latin-1 -*-
# A linha acima faz o sistema interpretar direito os acentos
# nas linhas de coment�rios
#
# programa problema12.py
# Verificar se um n�mero natural � triangular


def main():
    n = input("Digite um numero natural: ")

    if n<=0:
        print "O numero deve ser positivo!!!"
        return

    # id�ia da solu��o
    # come�ar com 1*2*3 e prosseguir com
    # 2*3*4, 3*4*5 e assim por diante
    # at� o produto de tr�s consecutivos
    # ficar maior ou igual a n

    a=1
    prod = a*(a+1)*(a+2)

    while prod<n :
        a = a+1
        prod = a*(a+1)*(a+2)

    if prod == n :
        print n, "e' triangular pois", n, "=", a, "*", a+1, "*", a+2
    else :
        print n, "nao e' triangular"
