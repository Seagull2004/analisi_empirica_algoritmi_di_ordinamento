import algoritmi.countingSort as CS
import algoritmi.quicksort as QS
import algoritmi.quicksort3Way as QS3
import algoritmi.radixSort as RS
import utils.measurement as measurement
import utils.geometricRangeGenerator as generatorRange
import matplotlib.pyplot as plt
import numpy as np

# Numero di misurazioni
range = 100

# Algoritmi e relative configurazioni
algorithms = [
    {"name": "Counting Sort", "algo": CS.uniformedCountingSort, "color": "black"},
    {"name": "Quick Sort", "algo": QS.uniformedQuickSort, "color": "black"},
    {"name": "Quick Sort 3-Way", "algo": QS3.uniformedQuickSort3Way, "color": "black"},
    {"name": "Radix Sort", "algo": RS.uniformedRadixSort, "color": "black"}, # da errore siccome il radix ha bisogno di elementi con lo stesso numero di cifre
]

# Creazione di sottotrame
plt.figure(figsize=(12, 10))  # Aumenta la dimensione della figura per adattarsi a più sottotrame

for idx, algo_config in enumerate(algorithms, start=1):
    ascisse = [0] * range
    ordinate = [ 0.0 ] * range
    count = 0

    for n in generatorRange.generateGeometricRange(100, 100000, range):
        ascisse[count] = n
        ordinate[count] = measurement.measureMeanTimeAlgo(algo_config["algo"], n, m=100000) # se n varia il range m è lockato a 100k
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
    plt.loglog(ascisse, fitted_y, linestyle='-', color='red', label='Curva di adattamento')
    plt.legend()

plt.tight_layout()
plt.show()

