# Programa para transformar uma imagem em sua transposta
#
import Image

# le imagem do arquivo
M = Image.open('.\Lena.png')
width , height = M.size
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"

# cria nova imagem e a preenche com transposta da imagem lida
T = Image.new('L', [width,height])
for i in range (width):
    for j in range (height):
        v = M.getpixel((i,j))
        T.putpixel((j,i),v)
        
T.show()
