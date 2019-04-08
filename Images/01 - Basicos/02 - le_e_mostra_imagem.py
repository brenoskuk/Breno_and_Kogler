# Programa para ler uma imagem em uma matriz M e exibir a matriz
#
import Image

M = Image.open('.\Lena.png')
print "tamanho = ", M.size , "pixels"
print "tipo = ", M.mode

M.show()
