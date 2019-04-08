# -*- coding: latin-1 -*-
#
# Programa selection_sort.py

# Programa que l� uma seq��ncia de n�meros inteiros e
# a imprime, em ordem crescente. A seq��ncia � ordenada
# usando-se um algoritmo conhecido por selection sort
# (ou ordena��o por sele��o)

#-------------------------------------------------------------
# OBSERVA��O: este programa cont�m mais coment�rios
#             do que c�digo propriamente dito. Por favor,
#             N�O tomem este como exemplo de documenta��o
#             de um programa.
#             A documenta��o de um programa deve ser feita
#             com o intuito de facilitar a sua leitura
#             e deve supor que o leitor conhece a linguagem
#             de programa��o (n�o se deve comentar o conhecido).
#             Aqui muito dos coment�rios s�o para explicar
#             detalhes da linguagem!
#-------------------------------------------------------------

# Id�ia do algoritmo:
# Repete-se um processo de forma que, ap�s a itera��o (rodada)
# de n�mero i, garante-se que todos os n�meros armazenados
# na lista das posi��es de �ndice 0 a i est�o ordenados e s�o
# os i+1 menores n�meros de toda a seq��ncia.
# (observe que as itera��es come�am em 0 e n�o em 1)
#
# Para isso, compara-se o n�mero na posi��o i com os n�meros
# nas demais posi��es maiores que i, e sempre que o n�mero na
# posi��o i for maior que o n�mero na outra posi��o, estes
# trocam de lugar entre si. (observe que enquanto a posi��o i
# fica fixa, o n�mero armazenado na posi��o i pode variar)
#
# - Ap�s a itera��o i=0, na posi��o 0 da lista estar� o menor
#   n�mero da seq.
# - Ap�s a itera��o i=1, nas duas primeiras posi��es da lista
#   estar�o os dois menores n�meros da seq., ordenados
# - Ap�s uma itera��o i qualquer, nas i+1 primeiras posi��es da 
#   lista estar�o os i+1 menores n�meros da seq., ordenados
# - Ap�s a itera��o i=n-2, a lista estar� ordenada.


# Fun��o selection_sort()
# Par�metros:
#     x (entrada/sa�da) : uma lista de inteiros (poderia ser de n�meros reais
#                         ou de letras)
# Valor de retorno: nenhum
def selection_sort(x):

    # calcula o tamanho da lista de entrada
    n = len(x)

    i=0
    while i < n-1 :

        # para uma posi��o i corrente, precisamos comparar
        # o n�mero armazenado em x[i] com os n�meros
        # armazenados em x[i+1],...,x[n-1]. Usamos
        # j para acessar essas posi��es posteriores a i
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

    # leitura da seq��ncia
    # Note que, aqui, diferente da forma usual, n�o � pedido o tamanho
    # da seq��ncia. Al�m disso, a seq��ncia toda deve ser digitada
    # em uma �nica linha
    entrada = raw_input("Digite uma sequencia de numeros separados por espaco e termine com ENTER\n")

    # entrada � uma string. N�o � uma lista de n�meros!!!
    # portanto, no la�o a seguir vamos extrair os n�meros dessa string


    seq = []   # cria uma lista vazia

    # na seguinte linha, entrada.split() tem o efeito de separar os 'tokens'
    # da string entrada e coloc�-los em uma lista.
    # Ent�o, percorre-se essa lista de tokens e para cada token
    # convertemos ele para n�mero e concatenamos � lista seq.
    for elemento in entrada.split():
        seq = seq + [int(elemento)]  


    # agora sim, os n�meros da seq��ncia digitada est�o armazenadas
    # na vari�vel seq (que � uma lista de inteiros)
    # Vamos orden�-la

    selection_sort(seq)




    # Pronto!
    # Agora imprimimos a lista ordenada e FIM!
    for i in range(len(seq)):
        print seq[i],

    print


# FIM


main()
