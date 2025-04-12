# qui metteremo delle funzioni che testano la CORRETTEZZA DEGLI ALGORITMI DI ORDINAMENTO
import utils.randomGenerator as generator
import algoritmi.quicksort as qs
import algoritmi.quicksort3Way as qs3
import algoritmi.countingSort as cs
import algoritmi.radixSort as rs
import random
import time 

NUMBER_OF_TESTS = 100
N_MIN           = 0
N_MAX           = 10000
M_MIN           = 0
M_MAX           = 100000

def isSorted(arr: list[int]) -> bool:
    """
    Controllo se la lista (array) passato in input è ordinato.

    Post:
        - True se arr è ordinato
        - False se esistono 0 <= i < j < len(arr) tali che A[i] > A[j]
    """
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

def test_quickSort():
    """
    Testa se il quick sort ha ordinato effettivamente un array disordinato

    Post:
        - se tutto viene ordinato correttamente stampa un messaggi di successo
    """
    t_in = time.perf_counter()
    for _ in range(NUMBER_OF_TESTS):
        n = random.randint(N_MIN, N_MAX)
        m = random.randint(M_MIN, M_MAX)
        vec = generator.generaArray(n, max = m)
        qs.quicksort(vec, 0, len(vec) - 1)
        if not isSorted(vec):
            print("Test su quick sort fallito dovrebbe essere ordinato")
            return
    t_out = time.perf_counter()
    print("Test superato in", round(t_out - t_in, 2), "s", "(quickSort)")


def test_quickSort3Way():
    """
    Testa se il quick sort 3 way ha ordinato effettivamente un array disordinato

    Post:
        - se tutto viene ordinato correttamente stampa un messaggi di successo
    """
    t_in = time.perf_counter()
    for _ in range(NUMBER_OF_TESTS):
        n = random.randint(N_MIN, N_MAX)
        m = random.randint(M_MIN, M_MAX)
        vec = generator.generaArray(n, m)
        qs3.quickSort3Way(vec)
        if not isSorted(vec):
            print(vec)
            print("Test su quick 3 way sort fallito")
            return
    t_out = time.perf_counter()
    print("Test superato in", round(t_out - t_in, 2), "s", "(quicksort3Way)")

def test_countingSort():
    """
    Testa se il counting sort ha ordinato effettivamente un array disordinato

    Post:
        - se tutto viene ordinato correttamente stampa un messaggi di successo
    """
    t_in = time.perf_counter()
    for _ in range(NUMBER_OF_TESTS):
        n = random.randint(N_MIN, N_MAX)
        m = random.randint(M_MIN, M_MAX)
        vec = generator.generaArray(n, max=m)
        B = [0 for _ in range(len(vec))]
        cs.countingSort(vec, B, m)
        if not isSorted(B):
            print(B)
            print("Test su counting sort fallito")
            return
    t_out = time.perf_counter()
    print("Test superato in", round(t_out - t_in, 2), "s", "(countingSort)")

def test_radixSort():
    """
    Testa se il radix sort ha ordinato effettivamente un array disordinato

    Post:
        - se tutto viene ordinato correttamente stampa un messaggi di successo
    """
    t_in = time.perf_counter()
    for _ in range(NUMBER_OF_TESTS):
        n = random.randint(N_MIN, N_MAX)
        m = random.randint(M_MIN, M_MAX)
        vec = generator.generaArray(n, max=m)
        rs.radixSort(vec)
        if not isSorted(vec):
            print(vec)
            print("Test su bucket sort fallito")
            return
    t_out = time.perf_counter()
    print("Test superato in", round(t_out - t_in, 2), "s", "(radixSort)")
