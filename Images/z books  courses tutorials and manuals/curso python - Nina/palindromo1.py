# -*- coding: latin-1 -*-
#
# Programa palindromo.py

# Programa que verifica se uma palavra ou frase � um pal�ndromo
# N�o desconsidera espa�os em branco nem pontua��o!!
# diferencia mai�scula de min�scula !

def main():

    s = input("Digite uma palavra ou frase: ")

    tam = len(s)
    print "A palavra/frase possui tamanho ", tam


    # ap�s a leitura da palavra/frase, procede-se
    # sucessivas compara��es caractere a caractere (primeiro
    # com o �ltimo, segundo com o pen�ltimo, e assim
    # por diante.

    # Essa compara��o � realizada at� que todos da metade
    # � esquerda tenham sido comparados com os respectivos
    # na metade da direita, ou at� descobrirmos que a
    # palavra/frase n�o � pal�ndromo.

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
