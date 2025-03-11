def mergeSort(A):
    if len(A) <= 0:
        return
    mergeSortAux(A, 0, len(A) - 1)

def mergeSortAux(A, p, q):  
	if (p < q):
		r = (p + q) // 2
		mergeSortAux(A, p, r) 
		mergeSortAux(A, r + 1, q) 
		merge(A, p, r, q)

def merge(A, p, r, q):
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
