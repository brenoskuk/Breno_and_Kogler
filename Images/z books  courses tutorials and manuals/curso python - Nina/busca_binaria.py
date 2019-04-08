# Funcao bubble_sort()
# Parametros:
#     x (entrada/saida) : uma lista de inteiros (poderia ser de numeros reais
#                         ou de letras)
# Valor de retorno: nenhum
def bubble_sort(x):

    # calcula o tamanho da lista de entrada
    n = len(x)

    r = 1
    while r < n :

        # j para acessar essas posicoes posteriores a i
        j=0
        while j < n-r :
            if x[j] > x[j+1] :
                aux = x[j]
                x[j] = x[j+1]
                x[j+1] = aux
            j=j+1

        r=r+1


def busca_binaria(v,x):
    n = len(x)

    e = 0
    d = n-1

    while (e <= d) : 

        m = (e + d)/2 

        if (x[m] == v):
            return m

        if (x[m] < v):
            e = m + 1
        else:
            d = m - 1
   
    return -1




def main():

    # leitura da sequencia
    entrada = raw_input("Digite uma sequencia de numeros separados por espaco e termine com ENTER\n")

    seq = []   # cria uma lista vazia

    # convertemos os elementos da string entrada
    # para numero e concatenamos `a lista seq.
    for elemento in entrada.split():
        seq = seq + [int(elemento)]  


    # Ordena

    bubble_sort(seq)

    print "Lista ordenada"
    for i in range(0,len(seq)):
        print seq[i],
    print


    v = input("Digite o numero a ser buscado: ")
    i = busca_binaria(v,seq)

    if i == -1:
        print "O numero buscado nao esta' na lista"
    else:
        print "O numero buscado esta na posicao ", i

#FIM
