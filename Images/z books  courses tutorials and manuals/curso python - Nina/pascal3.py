# -*- coding: latin-1 -*-
#
# Programa pascal3.py
# Vers�o 3: usa as fun��es fat() e comb()
# Note que n�o � muito diferente da Vers�o 2 !!


# Fun��o para c�lculo do fatorial de x
def fat(x):
    i=2
    f=1
    while i<=x:
        f=f*i
        i=i+1
    return f


# Fun��o para c�lculo da combina��o de n, i a i
def comb(n,i):
    return fat(n)/(fat(i)*fat(n-i))



# Programa principal: L� n e imprime o tri�ngulo de
# Pascal com n+1 linhas

def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return
    
    # linhas variam de 0 a n
    for i in range(0,n+1):

        # para a linha i, colunas variam de 0 a i 
        for j in range(0,i+1):
            print comb(i,j),

        print

# FIM


main()
