#                        _   _                              _
#   ___ ___  _   _ _ __ | |_(_)_ __   __ _   ___  ___  _ __| |_ 
#  / __/ _ \| | | | '_ \| __| | '_ \ / _` | / __|/ _ \| '__| __|
# | (_| (_) | |_| | | | | |_| | | | | (_| | \__ \ (_) | |  | |_ 
#  \___\___/ \__,_|_| |_|\__|_|_| |_|\__, | |___/\___/|_|   \__|
#                                    |___/

def countingSort(A: list[int], B: list[int], k: int) -> None:
    """
    Ordinamento countingSort classico

    Args:
        A: la lista da ordinare
        B: il vettore che dovrà contenere il risultato
        k: il valore massimo che posso trovare nella lista A
    Post:
        - B viene modificato in modo che sia ordinato in senso crescente
    """
    C = [0 for _ in range(k + 1)] # avrà lunghezza k+1 C[0..k]
    # fase di conto occorrenze
    for i in range(0, len(A)):
        C[A[i]] += 1
    # fase di settaggio indirizzi di inserimento (somma parziale)
    C[0] -= 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]    
    # fase di creazione risultato
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1


def uniformedCountingSort(A: list[int], k: int) -> list[int]:
    """
    versione ausiliaria di countingSort per avere solo input l'array da ordinare e il max

    Args:
        A: vettore da ordinare
        k: valore massimo che posso trovare all'interno di A

    Post:
        - Viene restituito un nuovo vettore che rappresenta la versione ordinata di A
    """
    B = [ 0 ] * len(A)
    countingSort(A, B, k)
    return B
