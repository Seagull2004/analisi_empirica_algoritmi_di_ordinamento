import algoritmi.mergeSort as MS
import algoritmi.countingSort as CS
import algoritmi.quicksort3Way as QS3
import algoritmi.quicksort as QS
import time
import random


print("mini test per il mergeSort")
A = [1,2,3,5,8,7,6,5,4,5,6,7,8,9,0,9,6,5,4,3,7,6,5,4,3,2]
MS.mergeSort(A)
print(A)
print("---")


print("mini test per il countingSort")
A = [1,2,3,5,8,7,6,5,4,5,6,7,8,9,0,9,6,5,4,3,7,6,5,4,3,2]
B = [0 for _ in range(len(A))]
CS.countingSort(A, B, len(A))
print(B)
print("---")


print("mini test per il quicksort3Way")
A = [1,2,3,5,8,7,6,5,4,5,6,7,8,9,0,9,6,5,4,3,7,6,5,4,3,2]
QS3.quickSort3Way(A)
print(A)
print("---")


print("mini test per il quickSort")
A = [1,2,3,5,8,7,6,5,4,5,6,7,8,9,0,9,6,5,4,3,7,6,5,4,3,2]
QS.quickSort(A)
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
