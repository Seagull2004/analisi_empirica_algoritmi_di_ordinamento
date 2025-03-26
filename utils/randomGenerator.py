# generatore pseudo casuale di array di dimensione arbitraria n e con valori numerici presenti nel range [1...m]
# todo
import random
import bisect

#input: len lunghezza array
#       max massimo valore elementi
#       disp: 0 per avere un array ordinato in ordine crescente
#             1 per un array ordinato in ordine decrescente
#             2 per un array con elementi disposti casualmente

def riempiOrdinato(len, max):
    elements = []
    for i in range(len):
        bisect.insort(elements, random.randint(0, max))

    return elements

def riempiCasualmente(len, max):
    elements = [0] * len
    for i in range(len):
        elements[i] = random.randint(0, max)

    return elements

def generaArray(len, max, disp):
    assert(len > 0)
    assert(disp == 0 or disp == 1 or disp == 2) 

    if disp == 0:
        return riempiOrdinato(len, max)
    elif disp == 1:
        arr = riempiOrdinato(len, max)
        arr.reverse()
        return arr
    else:
        return riempiCasualmente(len, max)   
