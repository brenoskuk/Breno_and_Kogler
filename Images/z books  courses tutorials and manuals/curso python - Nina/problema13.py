# -*- coding: latin-1 -*-
# A linha acima faz o sistema interpretar direito os acentos
# nas linhas de comentários
#
# programa problema13.py
# Contar o número de segmentos de números iguais consecutivos
# em uma seqüência de tamanho n


def main():
    n = input("Digite o tamanho da sequencia: ")

    if n<=0:
        print "O tamanho deve ser positivo!!!"
        return

    # idéia da solução
    # ler o primeiro número da seq. antes do laço
    # dentro do laço, ler o próximo número da seq.
    # e comparar com o anterior. Se forem diferentes,
    # trata-se do início de um novo segmento na seq.

    print "Digite os numeros da sequencia"
    # o primeiro número da seq. pode ser lido pois n>0
    ant = input("Primeiro numero: ")

    seg = 1 # há pelo menos um segmento na seq.
    i = 1 # contador para controlar a quantidade de
          # números já lidos da seq.

    while i<n :
        num = input("Proximo numero: ")
        if ant != num:
            seg = seg+1
            ant = num
        i = i+1

    print "Numero de segmentos = ", seg
