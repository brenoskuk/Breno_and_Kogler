# leitura do nome do arquivo
nome_arq = raw_input("Digite o arquivo a ser lido :")

if len(nome_arq)==0:
    nome_arq = "myfile.txt"

# abre arquivo para leitura
f = open(nome_arq, 'r')

#move o ponteiro para o inicio do arquivo
f.seek(0)

print "["
i = 0
for line in f:
    print line
    i = i+1
print "]"

print "\n\n>>> Ha' ", i, "linhas no arquivo"
