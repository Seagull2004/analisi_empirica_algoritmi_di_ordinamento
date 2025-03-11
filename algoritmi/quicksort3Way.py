def quickSort3Way(vec):
    if len(vec) <= 0:
        return
    quickSort3WayRec(vec, 0, len(vec))

def quickSort3WayRec(vec, p, q): 
    if q - p <= 1:
        return
    res = partition3way(vec, p, q)
    quickSort3WayRec(vec, p, res[0])
    quickSort3WayRec(vec, res[1], q)

def partition3way(A, p, q):
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
     
