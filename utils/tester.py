# qui metteremo delle funzioni che testano la correttezza degli algoritmi di ordinamento
from typing import List
import utils.randomGenerator as generator
import algoritmi.quicksort as qs
import algoritmi.quicksort3Way as qs3
import algoritmi.countingSort as cs
import algoritmi.radixSort as rs

def isSorted(arr: List):
    if len(arr) < 2:
        return True
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def test_quickSort():
    for _ in range(100):
        n = 10000
        m = 10000
        vec = generator.generaArray(n, max=m)
        qs.quickSort(vec)
        if not isSorted(vec):
            print("Test su quick sort fallito dovrebbe essere ordinato")
            return
    print("Test superato")


def test_quickSort3Way():
    for _ in range(100):
        n = 10000
        m = 10000
        vec = generator.generaArray(n, m)
        qs3.quickSort3Way(vec)
        if not isSorted(vec):
            print(vec)
            print("Test su quick 3 way sort fallito")
            return
    print("Test superato")

def test_countingSort():
    for _ in range(100):
        n = 10000
        m = 10000
        vec = generator.generaArray(n, max=m)
        B = [0 for _ in range(len(vec))]
        cs.countingSort(vec, B, m)
        if not isSorted(B):
            print(B)
            print("Test su counting sort fallito")
            return
    print("Test superato")

def test_radixSort():
    for _ in range(100):
        n = 10000
        min = 100
        m = 999
        vec = generator.generaArray(n, min=min, max=m)
        rs.radixSort(vec)
        if not isSorted(vec):
            print(vec)
            print("Test su bucket sort fallito")
            return
    print("Test superato")
