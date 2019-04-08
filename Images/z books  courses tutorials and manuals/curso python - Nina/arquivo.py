# -*- coding: latin-1 -*-
#
# Este programa ilustra algumas formas de ler e escrever
# de/para arquivos em Python e tamb�m um pouco de manipula��o de strings
# -----------------------------------------------------------
# Para melhor entender os comandos, experimente execut�-los
# individualmente no ambiente interativo do Python.
# L� voc� poder� ver o que est� armazenado nas vari�veis.
# -----------------------------------------------------------

def main():


    print ">>> Programa para ilustrar manipulacao de arquivos e strings"




# -----------------------------------------------------------------------------------------



    print ">>> Sera' criada um arquivo com o nome myfile.txt\n\n"

    # criar um arquivo e escrever nele.
    f = open("myfile.txt", 'w')

    texto = "Este e' um arquivo com 4 linhas.\nA primeira e segunda linhas contem frases comuns, a terceira e'uma linha vazia, e a quarta contem numeros.\n\n100 101 102 102\n"

    f.write(texto)

    f.close()


    print ">>> ja' foi criada!!\n\n"


# -----------------------------------------------------------------------------------------




    # leitura do nome do arquivo
    # o raw_input() considera exatamente aquilo que foi digitado
    # sem tentar 'interpret�-lo' (no caso do input(), por�m, se
    # for digitado 20, ele o transforma no n�mero 20)
  
    nome_arq = raw_input("Agora digite o nome de um arquivo texto, sem aspas (ENTER para ler myfile.txt): ")


    if len(nome_arq)==0:
        nome_arq = "myfile.txt"

    # abre arquivo para leitura
    f = open(nome_arq, 'r')




# -----------------------------------------------------------------------------------------



    print "\n\n>>> Leitura do arquivo, em uma unica string"

    # Leitura de todo o conte�do, devolvido em uma �nica string
    texto = f.read()
    #print texto

    print "\n\n>>> Numero de caracteres no texto: ", len(texto)

    print "["
    # separa as linhas armazenadas em texto
    linhas_texto = texto.splitlines()

    for line in linhas_texto:
        # remove caracteres \n no final da string
        line.strip('\n')
        print line

    print "]"

    x = raw_input("\n\nTecle ENTER")




# -----------------------------------------------------------------------------------------


    print "\n\n>>> Leitura do arquivo, em uma lista de strings"

    # Leitura de todo o conte�do, devolvido em uma lista de strings,
    # cada string correspondendo a uma linha do arquivo

    #move o ponteiro de volta para o inicio do arquivo
    f.seek(0)

    print "["
    linhas = f.readlines()
    for line in linhas:
        print line
    print "]"


    print "\n\n>>> Ha' ", len(linhas), "linhas no arquivo"


    x = raw_input("\n\n>>> Tecle ENTER")

    print "\n\n>>> Palavras da primeira linha"

    # Separa as palavras contidas na primeira linha,
    # que est� armazenada em linhas[0] (que ali�s deve ser
    # exatamente igual linhas_texto[0])
    prim_linha = linhas[0]
    palavras = prim_linha.split()

    print "["
    for pal in palavras:
        print pal
    print "]"


    x = raw_input("\n\n>>> Tecle ENTER")



# -----------------------------------------------------------------------------------------



    print "\n\n>>> Leitura do arquivo, linha a linha"


    # As duas formas acima l�em todo o conte�do e armazenam
    # na mem�ria. Se o aqruivo for muito grande, muito espa�o
    # de mem�ria de computador ser� necess�rio


    # Leitura linha a linha, at� o final do arquivo

    #move o ponteiro para o inicio do arquivo
    f.seek(0)

    print "["
    i = 0
    for line in f:
        print line
        i = i+1
    print "]"

    print "\n\n>>> Ha' ", i, "linhas no arquivo"


    x = raw_input("\n\nTecle ENTER")


    print "\n\n>>> Leitura do arquivo, apenas as 2 primeiras linhas"

    # Leitura linha a linha, das 5 primeiras linhas do arquivo

    #move o ponteiro para o inicio do arquivo
    f.seek(0)

    print "["
    for i in range(2):
        line = f.readline()
        print line
    print "]"


    x = raw_input("\n\nTecle ENTER")




# -----------------------------------------------------------------------------------------




    # fecha o arquivo. N�o mais poder� ser lida.
    f.close()    




# -----------------------------------------------------------------------------------------



    print "\n\n>>> Algumas operacoes com string"

    # cria uma string
    linha = "101 102 103 104"
    print linha

    # separa os tokens (subsequencia delimitada por caracteres separadores)
    # da linha e armazena em tokens
    # Note que tokens e' uma lista de strings
    print "\n\n>>>cada linha impressa a seguir e' uma string"

    tokens = linha.split()
    for token in tokens:
        print token

    # Como cada elemento da lista s�o strings de d�gitos,
    # os mesmos podem ser convertidos para n�meros 
    print "\n\n>>>cada linha impressa a seguir sao as strings acima convertidas para numeros"

    soma = 0
    for token in tokens:
        num = eval(token)
        print num
        soma = soma + num

    print "soma = ", soma


# FIM
# Experimente executar os comandos individualmente no ambiente interativo
# Para cada comando executado, veja o reultado. Por exemplo
# se executar
#
# > tokens = linha.split()
#
# veja o conte�do de linha e tokens digitando
#
# > linhas
# > tokens
#
# (o sinal > acima deve ser interpretado como o prompt do ambiente interativo)


main()
