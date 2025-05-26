import random
import bisect
from enum import Enum


class Disposition(Enum):
    """
    Enumerazione dei tipi di array generabili
    - RANDOM: array casuale
    - ASCENDANT: array già ordinato
    - DESCENDANT: array ordinato in senso inverso
    """
    RANDOM = 0
    ASCENDANT = 1
    DESCENDANT = 2


def riempiOrdinato(len: int, min: int, max: int) -> list[int]:
    """
    Genera un array ordinato con valori interi compresi tra min e max

    Args:
        len: numero di elementi prensenti nel vettore (0 o più)
        min: minimo valore che un elemento può assumere
        max: massimo valore che un elemento può assumere
    Post:
        - resituisce un array di lunghezza len
        - restituisce un array con valori compresi in [min:max]
        - l'array è ordinato in senso crescente
    """
    assert(min <= max)
    assert(len >= 0)
    newArray = []
    for _ in range(len):
        bisect.insort(newArray, random.randint(min, max))
    return newArray


def riempiCasualmente(len: int, min: int, max: int) -> list[int]:
    """
    Genera un array riempito casualmente con valori interi compresi tra min e max

    Args:
        len: numero di elementi prensenti nel vettore (0 o più)
        min: minimo valore che un elemento può assumere
        max: massimo valore che un elemento può assumere

    Post:
        - resituisce un array di lunghezza len 
        - restituisce un array con valori compresi in [0:max]
        - l'array ha gli elementi disposti in maniera casuale
    """
    assert(min <= max)
    assert(len >= 0)
    newArray = [ 0 ] * len
    for i in range(len):
        newArray[i] = random.randint(min, max)
    return newArray


def generaArray(len: int, max: int, min: int = 0, disp: Disposition = Disposition.RANDOM) -> list[int]:
    """
    Genera e restituisce un vettore arbitrario con un certo numero dato di elementi interi presenti nel range [min:max] e disposti in una certa posizione disp.

    Args: 
        len: lunghezza array (0 o più)
        max: massimo valore degli elementi
        min: minimo valore degli elementi
        disp: diposizione degli elementi dell'array

    Post:
        - restituisce un vettore di interi
        - il vettore restituito ha valore massimo <= max
        - il vettore restituito ha valore minimo >= min
        - il vettore restituito ha lunghezza len
        - il vettore restituito ha gli elementi disposti in maniera concorde a disp
    """
    assert(len >= 0)
    assert(min <= max)
    assert(isinstance(disp, Disposition))
    if disp == Disposition.ASCENDANT:
        return riempiOrdinato(len, min, max)
    if disp == Disposition.DESCENDANT:
        arr = riempiOrdinato(len, min, max)
        arr.reverse()
        return arr
    return riempiCasualmente(len, min, max)   
