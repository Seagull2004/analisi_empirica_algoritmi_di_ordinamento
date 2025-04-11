from typing import List

    
    

def quicksort(A: List[int], p: int, q: int) -> None:
    """
    Funzione ausiliaria per Quick Sort.
    
    Args: 
        0 <= p <= q < len(A)
    Post: 
        A[p...q - 1] viene ordinato
    """
    if (p < q):
        r = partition(A, p, q)
        quicksort(A, p, r - 1)
        quicksort(A, r + 1, q)

def partition(A: List[int], p: int, q: int) -> int:
    """
    Partiziona l'array A[p...q] intorno a un pivot A[q].
    
    Args:
        0 <= p <= q < len(A)
    Post: 
        - Tutti gli elementi a sinistra del pivot sono minori o uguali a esso
        - Tutti gli elementi a destra sono maggiori
    """
    i = p - 1
    x = A[q]
    for j in range(p, q + 1):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    return i

def uniformedQuickSort(A, k):
    """
        versione ausiliaria di quickSort per avere solo input l'array da ordinare e il max
        Ordina l'array A in ordine crescente usando Quick Sort.
    
        Args: 
            A è una lista di interi.
        Post: 
            A è ordinato in ordine non decrescente.
    """

    if len(A) <= 1:
        return
    quicksort(A, 0, len(A) - 1)

