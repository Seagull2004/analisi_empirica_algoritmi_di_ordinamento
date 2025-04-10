import random
import bisect
from enum import Enum

# Enumerazione dei tipi di array generabili
class Disposition(Enum):
    RANDOM = 0
    ASCENDANT = 1
    DESCENDANT = 2

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

def generaArray(len: int, max: int, min: int=0, disp: Disposition=Disposition.RANDOM):
    """
    Args: 
        len: lunghezza array
        max: massimo valore elementi
        min: minimo valore elementi
        disp: scegli come disporre gli elementi dell'array
            - Disposition.ASCENDANT per avere un array ordinato in ordine crescente
            - Disposition.DESCENDANT per un array ordinato in ordine decrescente
            - Disposition.RANDOM per un array con elementi disposti casualmente
    """
    assert(len > 0)
    assert(isinstance(disp, Disposition))

    if disp == Disposition.ASCENDANT:
        return riempiOrdinato(len, min, max)
    if disp == Disposition.DESCENDANT:
        arr = riempiOrdinato(len, min, max)
        arr.reverse()
        return arr
    return riempiCasualmente(len, min, max)   
