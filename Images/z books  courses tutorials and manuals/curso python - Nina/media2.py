# -*- coding: latin-1 -*-
# A linha acima faz o sistema interpretar direito os acentos
# programa media2.py

def main():

  print "Programa para calcular a nota media"

# inicializa a variável soma
  soma = 0

# Ler um número e imprimir
  n = input("Digite o numero de notas: ")

# Repetir n vezes 
  for i in range(n):
    num = input("Digite nota: ")
    soma = soma + num
    
# Calcular a média
  media = float(soma)/n

# Imprimir a média e parar
  print "A media e' ", media

# A linha abaixo evita que o sistema execute o programa quando importado 
if __name__ == "__main__": 
  main()
