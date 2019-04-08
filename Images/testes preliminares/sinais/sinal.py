# sinais especiais

from numpy import *

# funcao pente
def Pente(t,ta):
    pente = t-t
    
    for i in range(len(t)):
        chave = mod(i,a)
        if chave == 0:
            pente[i] = 1

    return pente

