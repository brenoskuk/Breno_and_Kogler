# -*- coding: latin-1 -*-
#
# Programa pascal2.py
# Versão 2: usa apenas a função fat()
# Veja como o código fica bem mais enxuto e limpo que o da Versão 1


# Função para cálculo do fatorial de x
def fat(x):
 
    i=2

    f=1
    while i<=x:
        f=f*i
        i=i+1

    return f





# Programa principal: Lê n e imprime o triângulo de
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
            print fat(i)/(fat(j)*fat(i-j)),

        print

# FIM


main()
