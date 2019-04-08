# Le arquivo contendo o nucleo de convolucao

from string import split

N = input("Entre a ordem do nucleo N x N com N impar: ")
L = (N-1)/2
# leitura do nome do arquivo do nucleo
nome_arq = raw_input("Digite o arquivo a ser lido :")
if len(nome_arq)==0:
    nome_arq = "nucleo.txt"
# abre arquivo para leitura
f = open(nome_arq, 'r')
#move o ponteiro para o inicio do arquivo
f.seek(0)

#transfere o nucleo lido para matriz G(i,j) de convolucao
G = []
for line in f:
    vals=line.split()
    Lin = []
    for j in range(N):
        Lin = Lin + [int(vals[j])]
    G = G + [Lin]
    
#imprime o nucleo de convolucao G(i,j)
for m in range(N):
    for n in range(N):
        print G[m][n],
    print
