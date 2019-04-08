# Programa para transformar uma imagem em seu negativo fotografico
#


import Image

# le image de um arquivo
M = Image.open('.\Lena.png')
width , height = M.size
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"

# cria nova imagem e a preenche com
#  o negativo da imagem lida = 255 - valor do pixel
N = Image.new('L', [width,height])
for i in range (width):
    for j in range (height):
        v = M.getpixel((i,j))
        N.putpixel((i,j),255 - v)
        
N.show()
