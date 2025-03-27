import random
import bisect
from enum import Enum

# Enumerazione dei tipi di array generabili
class Disposition(Enum):
    RANDOM = 0
    SORTED = 1
    SORTED_REV = 2

# resituisce un array di lunghezza len e con valori compresi in [0:max]
# l'array è ordinato in senso crescente
def riempiOrdinato(len: int, min: int, max: int):
    elements = []
    for _ in range(len):
        bisect.insort(elements, random.randint(min, max))
    return elements

# resituisce un array di lunghezza len e con valori compresi in [0:max]
# l'array ha gli elementi disposti in maniera casuale
def riempiCasualmente(len: int, min: int, max: int):
    elements = [0] * len
    for i in range(len):
        elements[i] = random.randint(min, max)
    return elements

def generaArray(len: int, min: int, max: int, disp: Disposition):
    """
    input: len lunghezza array
           min minimo valore elementi
           max massimo valore elementi
           disp: 0 per avere un array ordinato in ordine crescente
                 1 per un array ordinato in ordine decrescente
                 2 per un array con elementi disposti casualmente
    """
    assert(len > 0)
    assert(isinstance(disp, Disposition))

    if disp == Disposition.SORTED:
        return riempiOrdinato(len, min, max)
    if disp == Disposition.SORTED_REV:
        arr = riempiOrdinato(len, min, max)
        arr.reverse()
        return arr
    return riempiCasualmente(len, min, max)   
