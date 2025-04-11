import math

def generateGeometricRange(start, end, length) -> list:
    """
    Genera un intervallo geometrico di numeri da start a end con una lunghezza specificata.
    L'intervallo viene generato utilizzando una progressione geometrica.
    Argomenti:
        start (int): Il numero iniziale dell'intervallo.
        end (int): Il numero finale dell'intervallo.
        length (int): La lunghezza dell'intervallo.
    Restituisce:
        list: Una lista contenente l'intervallo geometrico di numeri.
    """

    A = start
    B = (end / start) ** (1 / (length-1))
    progression = [0] * length

    for i in range(length):
        progression[i] = math.floor(A * B ** i)

    return progression

