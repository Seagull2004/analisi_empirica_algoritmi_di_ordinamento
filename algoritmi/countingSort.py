from typing import List

def countingSort(A: List, B: List, k: int):
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



