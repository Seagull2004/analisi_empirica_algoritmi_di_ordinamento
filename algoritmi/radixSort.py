def estraiCifra(cifraDaEstrarre: int, n: int) -> int: 
    """
    Estrae una certa cifra (u, d, h, m ecc) da un numero n

    Args:
        cifraDaEstrarre: 0 unità, 1 decide, 2 centinaia, ...
    Post: 
        - restituisce la cifra richiesta del numero
        - restituisce 0 se la cifra non è esplictamente presente nel numero

    e.g.
        - estraiCifra(2, 1234) -> 2
        - estraiCifra(0, 1234) -> 4
        - estraiCifra(9, 1234) -> 0
        - estraiCifra(4, 1234) -> 0
    """
    cifreNumero = len(str(n))
    if cifreNumero < cifraDaEstrarre + 1:
        return 0
    return int(str(n)[cifreNumero - 1 - cifraDaEstrarre])


def radixSort(A: list[int], digits: int = -1) -> None:
    """
    Ordinamento radix sort del vettore A

    Args:
        A: una lista di interi che possiede solo numeri con lo stesso numero di cifre
        digits: il numero di cifre che hanno gli elementi (in particolare il valore massimo) se non viene passato come parametro o viene posto a -1 l'algoritmo troverà il massimo per poi stabilire il numero di digits da usare nell'algoritmo

    Post:
        A viene modificato in modo da essere ordinato
    """
    # caso base
    if len(A) <= 1:
        return
    # se non sappiamo il numero di cifre che ha il numero massimo lo calcoliamo Θ(n)!!
    if digits == -1:
        digits = len(str(max(A)))
    # frammentazione delle cifre in una matrice da usare nel radixSort
    matrix = [ [ estraiCifra(j, A[i]) for j in range(digits - 1, -1, -1) ] for i in range(len(A)) ]
    # ordinamento
    matrix = radixSortAux(matrix, digits, 10)
    # scrittura risultato nella lista fornita in input
    for i in range(len(matrix)):
        n = ""
        for j in range(len(matrix[i])):
            n += str(matrix[i][j])
        A[i] = int(n)
    

def radixSortAux(A: list[list[int]], digits: int, B: int) -> list[list[int]]:
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


def countingSort(A: list, k: int, cifraDaConsiderare: int) -> list[list[int]]:
    """
    Una versione del counting sort adattada per l'utilizzo del radix sort, basa l'ordinamento dei vettori della matrice su una cifra del numero (cifraDaConsiderare)

    Args:
        cifreDaConsiderare: la cifra (unità, decine, centinaia, ...) che considereremo nell'effettuare l'ordinamento
        0 = unità
        1 = decine
        2 = centinaia
        ...
    Post:
        - la matrice fornita in input non viene modificata
        - viene restituita una matrice risultato
    """
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


def uniformedRadixSort(A: list[int], k: int) -> None:
    """
    Versione ausiliaria di radixSort per avere solo input l'array da ordinare e il max

    Args:
        A: vettore di interi da ordinare
        k: valore massimo che posso trovare all'interno di A (non viene usato dal radix sort)

    Post:
        A viene ordianato in senso crescente
    """
    radixSort(A)

