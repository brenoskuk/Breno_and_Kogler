# Programa que calcula o produto escalar

# Programa principal
def main():

    print "Digite a dimensao dos vetores: "
    n = input()


    print "Digite o primeiro vetor: "
    entrada = raw_input()
    
    nums = entrada.split()
    V1 = list(eval(x) for x in nums)
    

    print "Digite o segundo vetor: "
    entrada = raw_input()
    
    nums = entrada.split()
    V2 = list(eval(x) for x in nums)
    

    if len(V1)!=len(V2):
        print "Vetores devem ter o mesmo tamanho!"
        return




    # Calcula o produto escalar
    soma = 0
    for i in range(len(V1)):
        soma = soma + V1[i]*V2[i]


 
    print "O produto escalar e' ", soma


# FIM
