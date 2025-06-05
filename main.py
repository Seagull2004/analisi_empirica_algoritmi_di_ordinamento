import matplotlib.pyplot as plt
import numpy as np
import json5
from time import sleep
from algoritmi.countingSort import uniformedCountingSort as countingSort
from algoritmi.quicksort import uniformedQuickSort as quickSort
from algoritmi.quicksort3Way import uniformedQuickSort3Way as quickSort3Way
from algoritmi.radixSort import uniformedRadixSort as radixSort
import utils.measurement as measurement
import utils.geometricRangeGenerator as generatorRange
from utils.randomGenerator import Disposition as Disposition
import os
import csv

# Alcuni parametri di configurazione
configuration = json5.load(open("./config.json"))
NUM_CAMPIONI = configuration["NUM_CAMPIONI"]
N_MIN        = configuration["N_MIN"]
N_MAX        = configuration["N_MAX"]
M_LOCK       = configuration["M_LOCK"]
M_MIN        = configuration["M_MIN"]
M_MAX        = configuration["M_MAX"]
N_LOCK       = configuration["N_LOCK"]


# Algoritmi e relative configurazioni
algorithms = [
    {"name": "Counting Sort", "algo": countingSort, "color": "#26547c", "ordinate": [], "ascisse": []},
    {"name": "Quick Sort", "algo": quickSort, "color": "#ef476f", "ordinate": [], "ascisse": []},
    {"name": "Quick Sort 3-Way", "algo": quickSort3Way, "color": "#ffd166", "ordinate": [], "ascisse": []},
    {"name": "Radix Sort", "algo": radixSort, "color": "#06d6a0", "ordinate": [], "ascisse": []},
]


def misuraTempiSullaBaseDi(variabile: str, var_end: int, lock: int, var_start: int = 0):
    """
    Args:
        variabile: 
                può essere 'n' o 'm' sulla base della variabile che si vuole far variare (n, numero di elementi degli array o m, range numerico degli elementi dell'array)
        var_start:
                valore di partenza di 'n' o 'm'
        var_end:
                valore di termine di 'n' o 'm'
        lock:
                il valore a cui si sceglie di lockare l'altra variabile (e.g. se si fa variare n da 0 a 100, m può essere lockata a 100k)
    """
    # ciclo sugli algoritmi che voglio cronometrare (countingSort, quicksort, ...)
    for idx, algo_config in enumerate(algorithms, start=1):
        # log sul terminale
        print("Inizio a misurare",algo_config["name"])

        # inizializzazione variabili
        ascisse = [ 0 ] * NUM_CAMPIONI
        ordinate = [ 0.0 ] * NUM_CAMPIONI
        measure_counter = 0

        # misurazione tempi
        for i in generatorRange.generateGeometricRange(var_start, var_end, NUM_CAMPIONI):
            ascisse[measure_counter] = i
            if variabile == 'n':
                ordinate[measure_counter] = measurement.measureMeanTimeAlgo(algo_config["algo"], n = i, m = lock, disposition = Disposition.RANDOM) 
            else:
                ordinate[measure_counter] = measurement.measureMeanTimeAlgo(algo_config["algo"], m = i, n = lock) 
            measure_counter += 1

        # salvataggio risultati nella struttura dati
        algo_config["ordinate"] = ordinate
        algo_config["ascisse"] = ascisse

        # scrittura su file CSV
        salvaRisultatiCSV(ascisse, ordinate, variabile, lock, algo_config["name"])


def salvaRisultatiCSV(ascisse, ordinate, variabile, lock, algo_name):
    """
    Salva i risultati delle misurazioni su file CSV.

    Args:
        ascisse: lista dei valori sull'asse x
        ordinate: lista dei valori sull'asse y (tempi)
        variabile: 'n' o 'm', la variabile che varia
        lock: valore della variabile bloccata
        algo_name: nome dell'algoritmo
    """
    altro = 'm' if variabile == 'n' else 'n'
    filename = f"{algo_name}_{variabile}_{altro}{lock}.csv"
    filepath = os.path.join("csv", filename)
    os.makedirs("csv", exist_ok=True)
    with open(filepath, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([variabile, "tempo_medio"])
        for x, y in zip(ascisse, ordinate):
            writer.writerow([x, y])


def stampaGraficiSeparatiDeiValoriMisurati(x_label: str, log_scale: bool=False, y_label: str="") -> None:
    """
    stampa il grafico dei valori che si trovano nella struttura dati globale algorithms

    Args:
        x_label: come nominare l'asse delle x del grafico
        log_scale: si può scegliere scalare gli assi
    """
    for idx, algo_config in enumerate(algorithms, start=1):
        plt.subplot(2,2,idx)
        # plot del grafico misurato
        plt.plot(algo_config["ascisse"], algo_config["ordinate"], marker='o', linestyle='', color=algo_config["color"], label=algo_config["name"])
        # plot del grafico teorico
        fitted_y = ottieniLineaTeorica(algo_config["ascisse"], algo_config["ordinate"])
        plt.plot(algo_config["ascisse"], fitted_y, linestyle='-', color=(algo_config["color"] + "20"))
        plt.xlabel(x_label)
        if y_label == "":
            plt.ylabel("t(" + x_label + ")") 
        else:
            plt.ylabel(y_label) 
        plt.legend()
        plt.tight_layout()
        if log_scale:
            plt.xscale("log")
            plt.yscale("log")
    plt.show()


def stampaGraficiVersus(x_label: str, log_scale: bool = False) -> None:
    """
    stampa una serie di grafici che permettdono di confrontare a due a due gli algoritmi
    """
    for i_1, algo_1 in enumerate(algorithms):
        for i_2 in range(i_1, len(algorithms)):
            algo_2 = algorithms[i_2]
            if algo_1["name"] == algo_2["name"]:
                continue
            # grafico primo algoritmo
            plt.plot(algo_1["ascisse"], algo_1["ordinate"], marker='o', linestyle='', color=algo_1["color"], label=algo_1["name"])
            # grafico teorico primo algoritmo
            plt.plot(algo_1["ascisse"], ottieniLineaTeorica(algo_1["ascisse"], algo_1["ordinate"]), linestyle='-', color=(algo_1["color"] + "20"))
            # grafico primo algoritmo
            plt.plot(algo_2["ascisse"], algo_2["ordinate"], marker='o', linestyle='', color=algo_2["color"], label=algo_2["name"])
            # grafico teorico secondo algoritmo
            plt.plot(algo_2["ascisse"], ottieniLineaTeorica(algo_2["ascisse"], algo_2["ordinate"]), linestyle='-', color=(algo_2["color"] + "20"))
            plt.xlabel(x_label)
            plt.ylabel("t(" + x_label + ")")
            plt.legend()
            if log_scale:
                plt.xscale("log")
                plt.yscale("log")
            plt.show()

def ottieniLineaTeorica(x, y):
    # plot del grafico teorico
    log_x = np.log10(x)
    log_y = np.log10(y)
    coeff = np.polyfit(log_x, log_y, 3)  # Fitting polinomiale di grado 3
    fitted_curve = np.poly1d(coeff)
    fitted_y = 10 ** fitted_curve(log_x) # Generazione dei valori della curva di adattamento
    return fitted_y

def stampaGraficoUnicoDeiValoriMisurati(x_label: str, log_scale: bool = False) -> None:
    """
    stampa il grafico dei valori che si trovano nella struttura dati globale algorithms

    Args:
        x_label: come nominare l'asse delle x del grafico
        log_scale: si può scegliere scalare gli assi
    """
    for idx, algo_config in enumerate(algorithms, start=1):
        # plot del grafico misurato
        plt.plot(algo_config["ascisse"], algo_config["ordinate"], marker='o', linestyle='', color=algo_config["color"], label=algo_config["name"])
        # plot del grafico teorico
        fitted_y = ottieniLineaTeorica(algo_config["ascisse"], algo_config["ordinate"])
        plt.plot(algo_config["ascisse"], fitted_y, linestyle='-', color=(algo_config["color"] + "20"))
    plt.xlabel(x_label)
    plt.ylabel('t(' + x_label + ')')
    plt.legend()
    if log_scale:
        plt.xscale("log")
        plt.yscale("log")
    plt.show()

def main():
    misuraTempiSullaBaseDi('n', var_start=N_MIN, var_end=N_MAX, lock=M_LOCK)
    stampaGraficoUnicoDeiValoriMisurati('n')
    stampaGraficiVersus('n')
    stampaGraficiSeparatiDeiValoriMisurati('n')

    misuraTempiSullaBaseDi('m', var_start=M_MIN, var_end=M_MAX, lock=N_LOCK)
    stampaGraficoUnicoDeiValoriMisurati('m')
    stampaGraficiVersus('m')
    stampaGraficiSeparatiDeiValoriMisurati('m')

main()
