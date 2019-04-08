from string import split

# leitura do nome do arquivo
nome_arq = raw_input("Digite o arquivo a ser lido :")

if len(nome_arq)==0:
    nome_arq = "myfile.txt"

# abre arquivo para leitura
f = open(nome_arq, 'r')

#move o ponteiro para o inicio do arquivo
f.seek(0)

M = []
i = 0
for line in f:
    vals=line.split()
    L = []
    for j in range(3):
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
