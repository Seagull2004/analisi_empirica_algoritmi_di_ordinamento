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
    quickSort3WayRec(vec, p, k)
    quickSort3WayRec(vec, l, q)


def partition3way(A: list[int], p: int, q: int) -> tuple[int, int]:
    """
    Partiziona l'array A[p...q - 1] in tre parti: minori, uguali e maggiori del pivot.
    #      p     k     l     q 
    # ... |<|<|<|=|=|=|>|>|>| ...

    Args: 
        0 <= p < q <= len(A)
    Post: 
        A[p...q - 1] viene diviso in tre sezioni ordinate correttamente.
        Vengono restituiti:
        - indice k: inizio partizione con elementi uguali al pivot
        - indice l: inizio partizione con elementi maggiori del pivot
    """
    pivot = A[p]
    k = p        # A[p..k-1] < pivot
    l = q        # A[l..q-1] > pivot
    j = p + 1    # A[k..j-1] == pivot

    while j < l:
        if A[j] < pivot:
            A[k], A[j] = A[j], A[k]
            k += 1
            j += 1
        elif A[j] > pivot:
            l -= 1
            A[j], A[l] = A[l], A[j]
        else:
            j += 1

    return k, l  # Elementi in A[k..l-1] == pivot

def uniformedQuickSort3Way(A: list[int], k: int) -> None:
    """
    Versione ausiliaria di quickSort3Way per avere solo input l'array da ordinare e il max

    Post:
        A viene ordinato in ordine crescente
    """
    quickSort3Way(A)

