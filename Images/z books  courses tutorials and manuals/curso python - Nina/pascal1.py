# -*- coding: latin-1 -*-
#
# Programa pascal1.py
# Vers�o sem uso de fun��o


# Programa principal: L� n e imprime o tri�ngulo de
# Pascal com n+1 linhas

def main():

    n = input("Digite um inteiro positivo: ")
    if n<=0:
        print "O numero deve ser positivo"
        return
    
    # linhas variam de 0 a n
    for i in range(0,n+1):

        # calcular fatorial de i
        fati = 1
        k = 2
        while k<=i:
            fati = fati*k
            k = k+1


        # para a linha i, colunas variam de 0 a i 
        for j in range(0,i+1):
            
            # calcula fatorial de j
            fatj = 1
            k = 2
            while k<=j:
                fatj = fatj*k
                k = k+1
            
            # calcular fatorial de i-j
            fatij = 1
            k = 2
            while k<=i-j:
                fatij = fatij*k
                k = k+1

            # calcular a combina��o de i, j a j e imprimir
            c = fati/(fatj*fatij)

            print c,  # a v�rgula faz com que o pr�ximo n�mero seja impresso na mesma linha

        print # este print faz com que o pr�ximo n�mero seja impresso na pr�xima linha

# FIM


main()
