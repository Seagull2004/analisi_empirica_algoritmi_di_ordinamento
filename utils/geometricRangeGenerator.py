import math

def generateGeometricRange(start: int, end: int, length: int = 100) -> list[int]:
    """
    Genera una successione geometrica contenente un numero di elementi pari a length
    La successione viene generato utilizzando una progressione geometrica.

    Args:
        start: Il numero iniziale dell'intervallo.
        end: Il numero finale dell'intervallo.
        length: La lunghezza dell'intervallo.

    Post:
        - restituisce una lista contenente i valori della successione geometrica che parte sta "start" e finisce con "end"
    """
    A = start
    B = (end / start) ** (1 / (length-1))
    progression = [0] * length
    for i in range(length):
        progression[i] = math.floor(A * B ** i)
    return progression
