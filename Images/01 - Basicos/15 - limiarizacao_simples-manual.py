# Programa para transformar uma imagem em sua transposta
#

import Image

# le imagem de arquivo
nome = raw_input("Digite o nome do arquivo - sem o .png - a ser lido :")
arq = '.\\' + nome + '.png'
print arq 
M = Image.open(arq)
#width , height = M.size

# obtem o limiar
L = input("Entre o valor do limiar entre 1 e 254: ")
print "Limiar manual = ", L

# IB imagem binarizada - valores 0 e 255
# M imagem original
IB = Image.new('L', [width,height])
for i in range (width):
    for j in range (height):
        v = M.getpixel((i,j))
        if v <= L :
            IB.putpixel((i,j),0)
        else:
            IB.putpixel((i,j),255)
            
IB.show()
