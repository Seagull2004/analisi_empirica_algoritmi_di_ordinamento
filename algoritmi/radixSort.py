
def radixSort(arr: list[int]) -> None:
    """
    Ordina in-place una lista di numeri interi non negativi usando il Radix Sort in base 10.
    
    Args:
        arr: Lista di interi da ordinare (non negativi).
    """
    if not arr:
        return

    # Trova il numero massimo per sapere il numero di cifre
    max_num = max(arr)
    exp = 1  # 10^0

    while max_num // exp > 0:
        couringSortByDigit(arr, exp)
        exp *= 10


def couringSortByDigit(arr: list[int], exp: int) -> None:
    """
    Counting sort basato sulla cifra a una certa posizione (exp).
    
    Args:
        arr: Lista da ordinare.
        exp: Esponente (1=unità, 10=decine, 100=centinaia,...)
    """
    n = len(arr)
    output = [0] * n
    C = [0] * 10  # 10 cifre decimali (0-9)

    # Conta le occorrenze delle cifre nella posizione corrente
    for num in arr:
        index = (num // exp) % 10
        C[index] += 1

    # Calcola le posizioni finali cumulative
    for i in range(1, 10):
        C[i] += C[i - 1]

    # Costruisci l'output ordinato (partendo dalla fine per stabilità)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[C[index] - 1] = arr[i]
        C[index] -= 1

    # Copia l'output nella lista originale
    for i in range(n):
        arr[i] = output[i]

def uniformedRadixSort(A: list[int], k: int) -> None:
    """
    Versione ausiliaria di radixSort per avere solo input l'array da ordinare e il max

    Args:
        A: vettore di interi da ordinare
        k: valore massimo che posso trovare all'interno di A (non viene usato dal radix sort)

    Post:
        A viene ordianato in senso crescente
    """
    radixSort(A)
