import algoritmi.countingSort as CS
import algoritmi.quicksort as QS
import algoritmi.quicksort3Way as QS3
import algoritmi.radixSort as RS
import utils.measurement as measurement
import utils.geometricRangeGenerator as generatorRange
import matplotlib.pyplot as plt
import numpy as np


# Alcuni parametri di configurazione
NUM_CAMPIONI = 100      # Quanti campioni vengono misurati per singolo algoritmo di ordinamento
N_MIN        = 100      # Se facciamo variare il numero di elementi (n) questo è il valore di partenza
N_MAX        = 100000   # Se facciamo variare il numero di elementi (n) questo è il valore di arrivo
M_LOCK       = 100000   # Se facciamo variare il numero di elementi (n) questo è il valore numerico massimo che gli elementi possono assumere
M_MIN        = 10       # Se facciamo variare i valori numerici degli elementi (m) questo è il valore di partenza
M_MAX        = 1000000  # Se facciamo variare i valori numerici degli elementi (m) questo è il valore di arrivo
N_LOCK       = 10000    # Se facciamo variare i valori numerici degli elementi (m) questo è il numero di elementi fisso che avranno i vari vettori


# Algoritmi e relative configurazioni
algorithms = [
    {"name": "Counting Sort", "algo": CS.uniformedCountingSort, "color": "black"},
    {"name": "Quick Sort", "algo": QS.uniformedQuickSort, "color": "black"},
    {"name": "Quick Sort 3-Way", "algo": QS3.uniformedQuickSort3Way, "color": "black"},
    {"name": "Radix Sort", "algo": RS.uniformedRadixSort, "color": "black"},
]


# Creazione di sottotrame
plt.figure(figsize=(12, 10))  # Aumenta la dimensione della figura per adattarsi a più sottotrame
# ciclo sugli algoritmi che voglio cronometrare (countingSort, quicksort, ...)
for idx, algo_config in enumerate(algorithms, start=1):
    # log
    print("Inizio a misurare",algo_config["name"])
    # inizializzazione variabili
    ascisse = [ 0 ] * NUM_CAMPIONI
    ordinate = [ 0.0 ] * NUM_CAMPIONI
    count = 0
    # misurazione tempi
    for n in generatorRange.generateGeometricRange(N_MIN, N_MAX, NUM_CAMPIONI):
        ascisse[count] = n
        ordinate[count] = measurement.measureMeanTimeAlgo(algo_config["algo"], n, m = M_LOCK) 
        count += 1
    # Creazione della sottotrama con una griglia 2x2
    plt.subplot(2, 2, idx)
    plt.loglog(ascisse, ordinate, marker='o', linestyle='', color=algo_config["color"], markersize=2)
    plt.title(f'Tempi di esecuzione di {algo_config["name"]}', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Numero di elementi')
    plt.ylabel('Tempo di esecuzione (s)')
    # Calcolo della curva di adattamento in scala logaritmica
    log_x = np.log10(ascisse)
    log_y = np.log10(ordinate)
    coeff = np.polyfit(log_x, log_y, 3)  # Fitting polinomiale di grado 3
    fitted_curve = np.poly1d(coeff)
    # Generazione dei valori della curva di adattamento
    fitted_y = 10**fitted_curve(log_x)
    # Aggiunta della curva di adattamento al grafico
    plt.loglog(ascisse, fitted_y, linestyle='-', color='#ff000020', label='Curva di adattamento')
    plt.legend()
plt.tight_layout()
plt.show()

