# -*- coding: latin-1 -*-
#
# Programa selection_sort.py

# Programa que lê uma seqüência de números inteiros e
# a imprime, em ordem crescente. A seqüência é ordenada
# usando-se um algoritmo conhecido por selection sort
# (ou ordenação por seleção)

#-------------------------------------------------------------
# OBSERVAÇÃO: este programa contém mais comentários
#             do que código propriamente dito. Por favor,
#             NÃO tomem este como exemplo de documentação
#             de um programa.
#             A documentação de um programa deve ser feita
#             com o intuito de facilitar a sua leitura
#             e deve supor que o leitor conhece a linguagem
#             de programação (não se deve comentar o conhecido).
#             Aqui muito dos comentários são para explicar
#             detalhes da linguagem!
#-------------------------------------------------------------

# Idéia do algoritmo:
# Repete-se um processo de forma que, após a iteração (rodada)
# de número i, garante-se que todos os números armazenados
# na lista das posições de índice 0 a i estão ordenados e são
# os i+1 menores números de toda a seqüência.
# (observe que as iterações começam em 0 e não em 1)
#
# Para isso, compara-se o número na posição i com os números
# nas demais posições maiores que i, e sempre que o número na
# posição i for maior que o número na outra posição, estes
# trocam de lugar entre si. (observe que enquanto a posição i
# fica fixa, o número armazenado na posição i pode variar)
#
# - Após a iteração i=0, na posição 0 da lista estará o menor
#   número da seq.
# - Após a iteração i=1, nas duas primeiras posições da lista
#   estarão os dois menores números da seq., ordenados
# - Após uma iteração i qualquer, nas i+1 primeiras posições da 
#   lista estarão os i+1 menores números da seq., ordenados
# - Após a iteração i=n-2, a lista estará ordenada.


# Função selection_sort()
# Parâmetros:
#     x (entrada/saída) : uma lista de inteiros (poderia ser de números reais
#                         ou de letras)
# Valor de retorno: nenhum
def selection_sort(x):

    # calcula o tamanho da lista de entrada
    n = len(x)

    i=0
    while i < n-1 :

        # para uma posição i corrente, precisamos comparar
        # o número armazenado em x[i] com os números
        # armazenados em x[i+1],...,x[n-1]. Usamos
        # j para acessar essas posições posteriores a i
        j=i+1
        while j < n :
            if x[i] > x[j] :
                aux = x[i]
                x[i] = x[j]
                x[j] = aux
            j=j+1

        i=i+1



# Programa principal
def main():

    # leitura da seqüência
    # Note que, aqui, diferente da forma usual, não é pedido o tamanho
    # da seqüência. Além disso, a seqüência toda deve ser digitada
    # em uma única linha
    entrada = raw_input("Digite uma sequencia de numeros separados por espaco e termine com ENTER\n")

    # entrada é uma string. Não é uma lista de números!!!
    # portanto, no laço a seguir vamos extrair os números dessa string


    seq = []   # cria uma lista vazia

    # na seguinte linha, entrada.split() tem o efeito de separar os 'tokens'
    # da string entrada e colocá-los em uma lista.
    # Então, percorre-se essa lista de tokens e para cada token
    # convertemos ele para número e concatenamos à lista seq.
    for elemento in entrada.split():
        seq = seq + [int(elemento)]  


    # agora sim, os números da seqüência digitada estão armazenadas
    # na variável seq (que é uma lista de inteiros)
    # Vamos ordená-la

    selection_sort(seq)




    # Pronto!
    # Agora imprimimos a lista ordenada e FIM!
    for i in range(len(seq)):
        print seq[i],

    print


# FIM


main()
