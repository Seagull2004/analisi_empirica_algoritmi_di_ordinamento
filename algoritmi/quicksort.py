def quickSort(A):
    if len(A) <= 1:
        return
    quickSortAux(A, 0, len(A) - 1)

def quickSortAux(A, p, q):
	if (p < q):
		r = partition(A, p, q)
		quickSortAux(A, p, r - 1)
		quickSortAux(A, r + 1, q)

def partition(A, p, q):
	i = p - 1
	x = A[q]
	for j in range(p, q + 1):
		if (A[j] <= x):
			i += 1
			A[i], A[j] = A[j], A[i]
	return i
