import time
from typing import Callable
import utils.randomGenerator as generator
from utils.randomGenerator import Disposition

def getResolution() -> float:
    """
    Ottieni la risoluzione del clock di sistema.
    Importante per trovare il tempo minimo misurabile

    Post: 
        Restituisce la risoluzione del clock di sistema
    """
    start = time.perf_counter()
    while(time.perf_counter() == start):
        pass
    stop = time.perf_counter()
    return stop - start

# Tempo minimo misurabile 
# (considerando l'errore massimo ammissibile E = 0.001)
#
# Tmin = R + (1/E + 1) 
#
# dove con R la risoluzione del clock di sistema
TMIN = getResolution() * 1001 

# Va posta nel ciclo che che scandisce il range di input desiderato
# Per il momento direi che possiamo lasciare dentro il tempo di generazione dell'array.
def measureMeanTimeAlgo(algo: Callable, n: int, m: int, k: int = 5, disposition: Disposition = Disposition.RANDOM) -> float:
    """
        Misura il tempo medio di esecuzione dell'algoritmo alg su un array lungo n con massimo valore m

        Args:
            algo: puntatore alla funzione da eseguire
            n: lunghezza input (numero elementi dell'array) da considerare
            m: massimo valore nell'input (valore massimo nell'array)
            k: numero di misurazioni richiesto 
            disposition: la disposizione dell'array da ordinare
        Post:
            potrebbero essere effettuate più di k misurazioni se le k misurazioni richieste vengono effettuate in meno tempo del tempo minimo misurabile, cosa che potrebbe avvenire probabilmente per input piccoli
    """
    count = 0 
    start_time = time.perf_counter()

    while True:
        a = generator.generaArray(n, m, disp = disposition) 
        algo(a,m) # cerchero' di uniformare gli algoritmi affinche' prendano tutti gli stessi input, eventualmente non utilizzati
        count += 1
        end_time = time.perf_counter()
        if end_time - start_time >= TMIN and count >= k:
            break
    return (end_time - start_time) / count
