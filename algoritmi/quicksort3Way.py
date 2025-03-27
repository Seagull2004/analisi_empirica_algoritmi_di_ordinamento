from typing import List, Tuple


# ciao mondo
def quickSort3Way(vec: List[int]) -> None:
    """
    Ordina l'array vec in ordine crescente usando il Quick Sort a 3 vie.
    
    Args:
        vec: List[int] è una lista.
    Post: 
        vec viene ordinato in ordine non decrescente.
    """
    if len(vec) < 2:
        return
    quickSort3WayRec(vec, 0, len(vec))

def quickSort3WayRec(vec: List[int], p: int, q: int) -> None: 
    """
    Funzione ricorsiva per il Quick Sort a 3 vie.
    
    Args: 
        0 <= p <= q <= len(vec)
    Post: 
        vec[p...q - 1] viene ordinato in ordine non decrescente.
    """
    if q - p < 2:
        return
    k, l = partition3way(vec, p, q)
    quickSort3WayRec(vec, p, k)
    quickSort3WayRec(vec, l, q)

def partition3way(A: List[int], p: int, q: int) -> Tuple[int, int]:
    """
    Partiziona l'array A[p...q - 1] in tre parti: minori, uguali e maggiori del pivot.
    #      p     k     l     q 
    # ... |<|<|<|=|=|=|>|>|>| ...
    
    Args: 
        0 <= p < q <= len(A)
    Post: 
        A[p...q - 1] viene diviso in tre sezioni ordinate correttamente.
    """
    if q - p < 1:
        return p, q

    pivot = A[q - 1]
    A[q-1], A[p] = A[p], A[q-1]
    k = p
    l = p
    for j in range(p + 1, q):
        # TOGLIERE I COMMENTI SOLO PER FARE DEBUG
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
    return k, l
