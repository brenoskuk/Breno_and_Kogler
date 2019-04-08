# -*- coding: latin-1 -*-
# A linha acima faz o sistema interpretar direito os acentos
# programa problema10.py

from math import sqrt

# solução mais ingênua possível
def main():
    print "Verifica se um numero e' primo de forma bem ingenua"
    p = input( "Digite um inteiro positivo: ")

    div = 2
    eh_primo=1
    iter = 0

    while div<p and eh_primo==1:
        iter = iter+1
        if p%div == 0:
            eh_primo=0
        else:
            div=div+1

    if eh_primo==1:
        print "O numero ", p, " e' primo."
    else:
        print "O numero ", p, " nao e' primo."

    print "\nLaco foi iterado ", iter, " vezes."



# solução um pouco experta
def main2():

    print "Verifica se um numero e' primo de forma um pouco experta"
    p = input( "Digite um inteiro positivo: ")

    div = 2
    eh_primo=1
    iter = 0

    while div<=p/2 and eh_primo==1:
        iter = iter+1
        if p%div == 0:
            eh_primo=0
        else:
            div=div+1

    if eh_primo==1:
        print "O numero ", p, " e' primo."
    else:
        print "O numero ", p, " nao e' primo."

    print "\nLaco foi iterado ", iter, " vezes."


# solução um pouco mais experta
def main3():

    print "Verifica se um numero e' primo de forma um pouco mais experta"
    p = input( "Digite um inteiro positivo: ")

    div = 2
    eh_primo=1
    iter = 0

    while div<=sqrt(p) and eh_primo==1:
        iter = iter+1
        if p%div == 0:
            eh_primo=0
        else:
            div=div+1

    if eh_primo==1:
        print "O numero ", p, " e' primo."
    else:
        print "O numero ", p, " nao e' primo."

    print "\nLaco foi iterado ", iter, " vezes."
