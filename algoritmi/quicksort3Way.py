#              _      _                   _     _____                    
#   __ _ _   _(_) ___| | _____  ___  _ __| |_  |___ /_      ____ _ _   _ 
#  / _` | | | | |/ __| |/ / __|/ _ \| '__| __|   |_ \ \ /\ / / _` | | | |
# | (_| | |_| | | (__|   <\__ \ (_) | |  | |_   ___) \ V  V / (_| | |_| |
#  \__, |\__,_|_|\___|_|\_\___/\___/|_|   \__| |____/ \_/\_/ \__,_|\__, |
#     |_|                                                          |___/ 
#

def quickSort3Way(vec: list[int]) -> None:
    """
    Ordina l'array vec in ordine crescente usando il Quick Sort a 3 vie.
    
    Args:
        vec: è la lista di interi che si vuole ordinare
    Post: 
        vec viene ordinato in ordine in ordine crescente
    """
    if len(vec) < 2:
        return
    quickSort3WayRec(vec, 0, len(vec))


def quickSort3WayRec(vec: list[int], p: int, q: int) -> None: 
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

    # Only recurse if subarray is non-empty
    if p < k:
        quickSort3WayRec(vec, p, k)
    if l < q:
        quickSort3WayRec(vec, l, q)
#    if q - p < 2:
#        return
#    k, l = partition3way(vec, p, q)
#    quickSort3WayRec(vec, p, k)
#    quickSort3WayRec(vec, l, q)


def partition3way(A: list[int], p: int, q: int) -> tuple[int, int]:
    """
    Partiziona l'array A[p...q - 1] in tre parti: minori, uguali e maggiori del pivot.
    #      p     k     l     q 
    # ... |<|<|<|=|=|=|>|>|>| ...
    
    Args: 
        0 <= p < q <= len(A)
    Post: 
        - A[p...q - 1] viene diviso in tre sezioni ordinate correttamente.
        - vengono restituiti:
          - indice di inizio partizione con elementi che hanno valore pari al pivot
          - indice di inizio partizione con elementi che hanno valore maggiore al pivot
    """
    pivot = A[p]
    lt = p        # A[p..lt-1] < pivot
    gt = q        # A[gt..q-1] > pivot
    i = p + 1     # A[lt..i-1] == pivot

    while i < gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            gt -= 1
            A[i], A[gt] = A[gt], A[i]
        else:
            i += 1

    return lt, gt  # Elements in A[lt..gt-1] == pivot
    if q - p < 1:
        return p, q
#    pivot = A[q - 1]
#    A[q-1], A[p] = A[p], A[q-1]
#    k = p
#    l = p
#    for j in range(p + 1, q):
#        # TOGLIERE I COMMENTI SOLO PER FARE DEBUG
#        # print(" ",end="")
#        # for x in range(i):
#        #     print("   ", end="")
#        # print("i")
#        # print(" ",end="")
#        # for x in range(j):
#        #     print("   ", end="")
#        # print("j")
#        # print(" ",end="")
#        # for x in range(k):
#        #     print("   ", end="")
#        # print("k")
#        # print(" ",end="")
#        # for x in range(l):
#        #     print("   ", end="")
#        # print("l")
#        # print(A)
#        if A[j] < pivot:
#            A[k], A[l] = A[l], A[k]
#            A[j], A[k] = A[k], A[j]
#            k += 1
#            l += 1
#        elif A[j] > pivot:
#            pass
#        else:
#            assert(A[j] == pivot)
#            A[l], A[j] = A[j], A[l]
#            l += 1
#    return k, l
#

def uniformedQuickSort3Way(A: list[int], k: int) -> None:
    """
    Versione ausiliaria di quickSort3Way per avere solo input l'array da ordinare e il max

    Post:
        A viene ordinato in ordine crescente
    """
    quickSort3Way(A)

