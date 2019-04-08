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
#transfere conteudo lido para matriz G(i,j) de convolucao
M = []
i = 0
for line in f:
    vals=line.split()
    L = []
    for j in range(N):
        L = L + [int(vals[j])]
    M = M + [L]
    i = i+1

print "\n\n>>> Ha' ", i, "linhas no arquivo"

print M

m = len(M)
n = len(M[0])

for i in range(m):
    for j in range(n):
        print M[i][j],
    print
