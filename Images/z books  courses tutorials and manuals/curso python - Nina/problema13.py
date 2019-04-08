# -*- coding: latin-1 -*-
# A linha acima faz o sistema interpretar direito os acentos
# nas linhas de coment�rios
#
# programa problema13.py
# Contar o n�mero de segmentos de n�meros iguais consecutivos
# em uma seq��ncia de tamanho n


def main():
    n = input("Digite o tamanho da sequencia: ")

    if n<=0:
        print "O tamanho deve ser positivo!!!"
        return

    # id�ia da solu��o
    # ler o primeiro n�mero da seq. antes do la�o
    # dentro do la�o, ler o pr�ximo n�mero da seq.
    # e comparar com o anterior. Se forem diferentes,
    # trata-se do in�cio de um novo segmento na seq.

    print "Digite os numeros da sequencia"
    # o primeiro n�mero da seq. pode ser lido pois n>0
    ant = input("Primeiro numero: ")

    seg = 1 # h� pelo menos um segmento na seq.
    i = 1 # contador para controlar a quantidade de
          # n�meros j� lidos da seq.

    while i<n :
        num = input("Proximo numero: ")
        if ant != num:
            seg = seg+1
            ant = num
        i = i+1

    print "Numero de segmentos = ", seg
