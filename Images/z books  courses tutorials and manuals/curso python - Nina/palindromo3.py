# -*- coding: latin-1 -*-
#
# Programa palindromo3.py

# Programa que verifica se uma palavra ou frase � um pal�ndromo
# Copia a palavra/frase invertida em outra string e em seguida
# compara a original com a c�pia invertida.
#
# N�o desconsidera espa�os em branco nem pontua��o!!
# N�o diferencia mai�scula de min�cula !

def main():

    frase = input("Digite uma palavra ou frase: ")

    tam = len(frase)
    print "A palavra/frase possui tamanho ", tam


    frase = frase.upper()   # converte para mai�scula
    fraseinvertida = ""     # cria string vazia


    # atribui � fraseinvertida os caracteres de frase
    # tomados de tr�s para a frente
    i = 0
    while i<tam:
        fraseinvertida = fraseinvertida + frase[tam-i-1]
        i = i+1


    # compara a frase com a fraseivertida
    if frase == fraseinvertida:
        print "E' palindromo"
    else:
        print "Nao e' palindromo"


# FIM


main()
