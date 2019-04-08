# -*- coding: latin-1 -*-
#
# Programa pascal1.py
# Versão sem uso de função


# Programa principal: Lê n e imprime o triângulo de
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

            # calcular a combinação de i, j a j e imprimir
            c = fati/(fatj*fatij)

            print c,  # a vírgula faz com que o próximo número seja impresso na mesma linha

        print # este print faz com que o próximo número seja impresso na próxima linha

# FIM


main()
