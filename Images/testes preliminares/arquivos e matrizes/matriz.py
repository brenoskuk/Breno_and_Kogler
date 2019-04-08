# funcoes para leitura, escrita e criacao de matriz


# Funcao para leitura de uma matriz m x n
def LeMatriz(m,n):
    M = []
    
    for i in range(m):
        entrada = raw_input("Linha %d: " % i)
        nums = entrada.split()
        L = []
        for j in range(n):
            L = L + [int(nums[j])]

        M = M + [L]

    return  M   


# Funcao para impressao de uma matriz M
def ImprimeMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print M[i][j],
        print



# Funcao para alocar uma matrix m x n
def CriaMatrizVazia(m,n):

    M = []

    for i in range(m) :

        L = []

        for j in range(n):
            L = L + [0]

        M = M + [L]

    return M




