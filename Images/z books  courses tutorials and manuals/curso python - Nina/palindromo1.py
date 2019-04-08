# -*- coding: latin-1 -*-
#
# Programa palindromo.py

# Programa que verifica se uma palavra ou frase é um palíndromo
# Não desconsidera espaços em branco nem pontuação!!
# diferencia maiúscula de minúscula !

def main():

    s = input("Digite uma palavra ou frase: ")

    tam = len(s)
    print "A palavra/frase possui tamanho ", tam


    # após a leitura da palavra/frase, procede-se
    # sucessivas comparações caractere a caractere (primeiro
    # com o último, segundo com o penúltimo, e assim
    # por diante.

    # Essa comparação é realizada até que todos da metade
    # à esquerda tenham sido comparados com os respectivos
    # na metade da direita, ou até descobrirmos que a
    # palavra/frase não é palíndromo.

    i=0
    eh_pal = 1

    while i<tam/2 and eh_pal==1:
        if s[i] != s[tam-i-1]:
            eh_pal = 0
        else:
            i = i+1

    if eh_pal == 1:
        print "E' palindromo"
    else:
        print "Nao e' palindromo"

# FIM


main()
