def quickSort(A):
    """
    Ordina l'array A in ordine crescente usando Quick Sort.
    
    Precondizione: A è una lista.
    Postcondizione: A è ordinato in ordine non decrescente.
    """
    if len(A) <= 1:
        return
    quickSortAux(A, 0, len(A) - 1)

def quickSortAux(A, p, q):
    """
    Funzione ausiliaria per Quick Sort.
    
    Precondizione: 0 <= p <= q < len(A)
    Postcondizione: A[p...q] è ordinato in ordine non decrescente.
    """
    if (p < q):
        r = partition(A, p, q)
        quickSortAux(A, p, r - 1)
        quickSortAux(A, r + 1, q)

def partition(A, p, q):
    """
    Partiziona l'array A[p...q] intorno a un pivot A[q].
    
    Precondizione: 0 <= p <= q < len(A)
    Postcondizione: Tutti gli elementi a sinistra del pivot sono minori o uguali a esso, mentre tutti gli elementi a destra sono maggiori.
    """
    i = p - 1
    x = A[q]
    for j in range(p, q + 1):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    return i
