import time
from randomGenerator import Disposition
import randomGenerator as generator

#Questa funzione fornisce la risoluzione del clock di sistema
#importante per trovare il tempo minimo misurabile
def getResolution():
    start = time.perf_counter()
    
    while(time.perf_counter() == start):
        pass
    stop = time.perf_counter()

    return stop - start

#Tempo minimo misurabile considerando l'errore massimo ammissibile E = 0.001
# Tmin = R + (1/E + 1) dove con R la risoluzione del clock di sistema
tmin = getResolution() * 1001 

#Questa funzione ha il compito di misurare il tempo medio ,su un certo numero di esecuzioni, di un dato algoritmo
#su un array di lunghezza n e con massimo valore m. Va posta nel ciclo che che scandisce il range di input desiderato
#Per il momento direi che possiamo lasciare dentro il tempo di generazione dell'array.
def measureMeanTimeAlgo(algo, n, m, k = 5, disposition = Disposition.RANDOM):
    """
        Misura il tempo medio di esecuzione dell'algoritmo alg su un array lungo n
        con massimo valore m

        algo:
            puntatore alal funzione da eseguire

        n:
            lunghezza input da considerare
        m:
            massimo valore nell'input
        k:
            numero di misurazioni richiesto (potrebbero essere effettuate piu' misurazioni se le k misurazioni sono effettuate in meno tempo del tempo minimo misurabile, probabilmente per input piccoli)
        disposition:
            in che modo e' ordinato l'input
    """
    count = 0 
    start_time = time.perf_counter()

    while True:
        a = generator.generaArray(n, m, disp = disposition) 
        algo(a,m) # cerchero' di uniformare gli algoritmi affinche' prendano tutti gli stessi input, eventualmente non utilizzati
        count += 1
        end_time = time.perf_counter()
        if end_time - start_time >= tmin and count >= k:
            break
    return (end_time - start_time) / count

