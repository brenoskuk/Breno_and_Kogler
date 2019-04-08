# -*- coding: latin-1 -*-
#
# Programa palindromo3.py

# Programa que verifica se uma palavra ou frase é um palíndromo
# Copia a palavra/frase invertida em outra string e em seguida
# compara a original com a cópia invertida.
#
# Não desconsidera espaços em branco nem pontuação!!
# Não diferencia maiúscula de minúcula !

def main():

    frase = input("Digite uma palavra ou frase: ")

    tam = len(frase)
    print "A palavra/frase possui tamanho ", tam


    frase = frase.upper()   # converte para maiúscula
    fraseinvertida = ""     # cria string vazia


    # atribui à fraseinvertida os caracteres de frase
    # tomados de trás para a frente
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
