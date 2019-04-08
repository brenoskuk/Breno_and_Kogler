# Programa que multiplica matrizes

from string import split
from matriz import *


def MultiMat(A,B,C):

    m = len(A)
    n = len(B)
    p = len(B[0])

    for i in range(m):
        for j in range(p):
            C[i][j] = 0
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]



# Programa principal
def main():

    print "Digite m,n,p , separado por espaco: "
    entrada = raw_input()

    # separar m de n e colocar nas respectivas variaveis
    x = entrada.split()
    m,n,p = int(x[0]),int(x[1]),int(x[2])
    
    # ou 
    # m,n,p = map(int, entrada.split())



    print "Digite a primeira matriz %d x %d, linha a linha" %(m,n)

    A = LeMatriz(m,n)



    print "Digite a segunda matriz %d x %d, linha a linha" %(n,p)

    B = LeMatriz(n,p)




    C = CriaMatrizVazia(m,p)

    MultiMat(A,B,C)


    
    print "A matriz produto e':"

    ImprimeMatriz(C)




# FIM
