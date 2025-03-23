def quickSort3Way(vec):
    """
    Ordina l'array vec in ordine crescente usando il Quick Sort a 3 vie.
    
    Precondizione: vec è una lista.
    Postcondizione: vec è ordinato in ordine non decrescente.
    """
    if len(vec) <= 0:
        return
    quickSort3WayRec(vec, 0, len(vec))

def quickSort3WayRec(vec, p, q): 
    """
    Funzione ricorsiva per il Quick Sort a 3 vie.
    
    Precondizione: 0 <= p <= q <= len(vec)
    Postcondizione: vec[p...q] è ordinato in ordine non decrescente.
    """
    if q - p <= 1:
        return
    res = partition3way(vec, p, q)
    quickSort3WayRec(vec, p, res[0])
    quickSort3WayRec(vec, res[1], q)

def partition3way(A, p, q):
    """
    Partiziona l'array A[p...q] in tre parti: minori, uguali e maggiori del pivot.
    
    Precondizione: 0 <= p < q <= len(A)
    Postcondizione: A[p...q] è diviso in tre sezioni ordinate correttamente.
    """
    if q - p <= 0:
        return
    # ora la situazione è come segue
    #      i     k     l     j 
    # ... |<|<|<|=|=|=|>|>|>| ...
    i = p
    k = p
    l = p

    for j in range(p, q - 1):
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

        if A[j] < A[q - 1]:
            A[k], A[l] = A[l], A[k]
            A[j], A[k] = A[k], A[j]
            k += 1
            l += 1
        elif A[j] > A[q - 1]:
            pass
        else:
            assert(A[j] == A[q - 1])
            A[l], A[j] = A[j], A[l]
            l += 1
    A[l], A[q - 1] = A[q - 1], A[l]
    l += 1
    return [k,l]
