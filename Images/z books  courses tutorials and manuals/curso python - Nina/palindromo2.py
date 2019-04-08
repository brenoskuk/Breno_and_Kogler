# -*- coding: latin-1 -*-
#
# Programa palindromo2.py

# Programa que verifica se uma palavra ou frase é um palíndromo
# Não desconsidera espaços em branco nem pontuação!!
# Não diferencia maiúscula de minúcula !

def main():

    s = input("Digite uma palavra ou frase: ")

    tam = len(s)
    print "A palavra/frase possui tamanho ", tam

    s = s.upper() # converte para maiúscula

    i = 0
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
