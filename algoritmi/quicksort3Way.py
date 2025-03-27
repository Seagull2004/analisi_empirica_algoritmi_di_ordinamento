from typing import List

def quickSort3Way(vec: List):
    """
    Ordina l'array vec in ordine crescente usando il Quick Sort a 3 vie.
    
    Precondizione: vec è una lista.
    Postcondizione: vec è ordinato in ordine non decrescente.
    """
    if len(vec) < 2:
        return
    quickSort3WayRec(vec, 0, len(vec))

def quickSort3WayRec(vec: List, p: int, q: int): 
    """
    Funzione ricorsiva per il Quick Sort a 3 vie.
    
    Precondizione: 0 <= p <= q <= len(vec)
    Postcondizione: vec[p...q-1] è ordinato in ordine non decrescente.
    """
    if q - p < 2:
        return
    k, l = partition3way(vec, p, q)
    quickSort3WayRec(vec, p, k)
    quickSort3WayRec(vec, l, q)

def partition3way(A: List, p: int, q: int):
    """
    Partiziona l'array A[p...q] in tre parti: minori, uguali e maggiori del pivot.
    
    Precondizione: 0 <= p < q <= len(A)
    Postcondizione: A[p...q] è diviso in tre sezioni ordinate correttamente.
    """
    if q - p < 1:
        return (p, q)
    # ora la situazione è come segue
    #      i     k     l     j 
    # ... |<|<|<|=|=|=|>|>|>| ...
    pivot = A[q - 1]
    A[q-1], A[p] = A[p], A[q-1]
    k = p
    l = p
    for j in range(p + 1, q):
        # print(" ",end="")
        # for x in range(i):
        #     print("   ", end="")
        # print("i")
        # print(" ",end="")
        # for x in range(j):
        #     print("   ", end="")
        # print("j")
        # print(" ",end="")
        # for x in range(k):
        #     print("   ", end="")
        # print("k")
        # print(" ",end="")
        # for x in range(l):
        #     print("   ", end="")
        # print("l")
        # print(A)

        if A[j] < pivot:
            A[k], A[l] = A[l], A[k]
            A[j], A[k] = A[k], A[j]
            k += 1
            l += 1
        elif A[j] > pivot:
            pass
        else:
            assert(A[j] == pivot)
            A[l], A[j] = A[j], A[l]
            l += 1
    return (k,l)
