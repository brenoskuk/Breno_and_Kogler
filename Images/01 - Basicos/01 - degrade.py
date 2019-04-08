# Programa para criar uma imagem contendo um degrade de tons de cinza
#

import Image

# tamanho da imagem a ser criada
width = 256
height = 256

# cria nova imagem e a preenche com degrade = media dos indices
I = Image.new('L', [width,height])
for i in range (width):
    for j in range (height):
        v=(i+j)/2
        I.putpixel((i,j),v)
        
I.show()
