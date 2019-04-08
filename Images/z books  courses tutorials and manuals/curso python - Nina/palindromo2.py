# -*- coding: latin-1 -*-
#
# Programa palindromo2.py

# Programa que verifica se uma palavra ou frase � um pal�ndromo
# N�o desconsidera espa�os em branco nem pontua��o!!
# N�o diferencia mai�scula de min�cula !

def main():

    s = input("Digite uma palavra ou frase: ")

    tam = len(s)
    print "A palavra/frase possui tamanho ", tam

    s = s.upper() # converte para mai�scula

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
