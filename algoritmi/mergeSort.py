def mergeSort(A):
    """
    Ordina l'array A in ordine crescente usando il Merge Sort.
    
    Precondizione: A è una lista.
    Postcondizione: A è ordinato in ordine non decrescente.
    """
    if len(A) <= 0:
        return
    mergeSortAux(A, 0, len(A) - 1)

def mergeSortAux(A, p, q):  
    """
    Funzione ausiliaria per il Merge Sort.
    
    Precondizione: 0 <= p <= q < len(A)
    Postcondizione: A[p...q] è ordinato in ordine non decrescente.
    """
	if (p < q):
		r = (p + q) // 2
		mergeSortAux(A, p, r) 
		mergeSortAux(A, r + 1, q) 
		merge(A, p, r, q)

def merge(A, p, r, q):
    """
    Unisce due sottoarray ordinati di A: A[p...r] e A[r+1...q].
    
    Precondizione: A[p...r] e A[r+1...q] sono ordinati in ordine non decrescente.
    Postcondizione: A[p...q] è ordinato in ordine non decrescente.
    """
    B = [0] * (q - p + 1)
    k = 0 # indice di inserimento in B
    i = p # indice di lettura A[p...r]
    j = r + 1 # indice di lettura A[r+1...q]

    # popolamento B
    for k in range(0, q - p + 1):
        if i > r:
            B[k] = A[j]
            j += 1
        elif j > q:
            B[k] = A[i]
            i += 1
        elif A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
    # copia B in A 
    for k in range(0, q - p + 1):
        A[p + k] = B[k]
