from typing import List

def radixSort(A: List[int]) -> None:
    if len(A) <= 1:
        return
    cifreElementi = len(str(A[0]))
    # frammentazione degli delle cifre in una matrice da usare nel radixSort
    matrix = [ [ int(str(A[i])[j]) for j in range(cifreElementi) ] for i in range(len(A)) ]
    matrix = radixSortAux(matrix, cifreElementi, 10)
    for i in range(len(matrix)):
        n = ""
        for j in range(len(matrix[i])):
            n += str(matrix[i][j])
        A[i] = int(n)
    

def radixSortAux(A: List[List[int]], digits: int, B: int) -> List[List[int]]:
    """
    Args:
        A : matrice da ordinare (ogni riga è un numero di digits cifre)
        digits : il numero di cifre che ha ogni numero (i.e. larghezza matrice)
        B : base numerica
    """
    k = B - 1
    for d in range(digits - 1, -1, -1):
        A = countingSort(A, k, d) 
    return A

# cifreDaConsiderare: la cifra (unità, decine, centinaia, ...) che considereremo nell'effettuare l'ordinamento
def countingSort(A: List, k: int, cifraDaConsiderare: int) -> List[List[int]]:
    # inizializzo array contatore
    C = [0] * (k + 1)
    # inizializzo array risultato
    B = [ [0] * len(A[0]) ] * len(A)
    # conto le occorrenze
    for i in range(0, len(A)):
        C[A[i][cifraDaConsiderare]] += 1
    # somme parziali
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # costruzione nuovo array a ritroso per garantire stabilità
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i][cifraDaConsiderare]] - 1] = A[i] # è necessario il -1 per trovare il corrento indirizzo in B, siccome gli indici partono da 0 e in B ci sono esattamente len(A) elementi, se in B ci fossero stato len(A) + 1 elementi il -1 sarebbe potuto essere tolto
        C[A[i][cifraDaConsiderare]] -= 1
    return B

