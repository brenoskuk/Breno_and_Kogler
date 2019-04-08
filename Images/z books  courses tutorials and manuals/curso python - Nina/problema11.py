# -*- coding: latin-1 -*-
# A linha acima faz o sistema interpretar direito os acentos
# programa problema11.py
# Cálculo de MDC


def main():
    a = input("Digite um inteiro positivo: ")
    b = input("Digite outro inteiro positivo: ")

    # coloca o maior em dividendo e o menor em divisor
    if a>b:
        dividendo = a
        divisor = b
    else:
        dividendo = b
        divisor = a

    # algoritmo de Euclides (até resto zero)
    resto = dividendo%divisor
    while resto != 0:
        dividendo = divisor
        divisor = resto
        resto = dividendo%divisor


    print "mdc(",a,",",b,") = ", divisor

