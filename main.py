import algoritmi.countingSort as CS
import algoritmi.quicksort3Way as QS3
import algoritmi.quicksort as QS
import algoritmi.radixSort as RS
import utils.randomGenerator as generator
from utils.randomGenerator import Disposition
import time
import random


print("mini test per il countingSort")
A = generator.generaArray(26, 10, Disposition.RANDOM)
print(A)
B = [0 for _ in range(len(A))]
CS.countingSort(A, B, len(A))
print(B)
print("---")


print("mini test per il quicksort3Way")
A = generator.generaArray(26, 10, Disposition.RANDOM)
print(A)
QS3.quickSort3Way(A)
print(A)
print("---")


print("mini test per il quickSort")
A = generator.generaArray(26, 10, Disposition.RANDOM)
print(A)
QS.quickSort(A)
print(A)
print("---")

print("mini test per il radixSort")
A = [123,587,654,567,890,965,437,654,321]
print(A)
RS.radixSort(A)
print(A)
print("---")

#for lunghezza in range(1000, 10000000, 10000):
#    A = [random.randrange(6) for _ in range(lunghezza)]
#    B = [0 for _ in range(len(A))]
#
#    start = time.perf_counter()
#    while time.perf_counter() == start:
#        pass
#    CS.countingSort(A, B, 6)
#    stop = time.perf_counter()
#    print(lunghezza, ";", stop - start)
