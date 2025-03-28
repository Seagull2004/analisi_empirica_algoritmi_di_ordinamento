
# Progetto di laboratorio

## Spiegazione da elearning

### Parametri
- $n$ lunghezza array (da 100 a 100k)
- $m$ range numerico dei valori dell'array (da 10 e 1M)

### Grafici
$n$ o $m$ sull'ascissa (x) e il tempo sull'ordinata (y) in modo da permettere la comparazione tra i vari algoritmi.

- se $n$ è l'ascissa:
	- 🔒 $m=100k$
- se $m$ è l'ascissa:
	- :lock: $n=10k$

#### Maggiori info

Ogni grafico deve essere composto da almeno 100 campioni, dove ogni campione rappresenta un possibile valore per l'ascissa (x).

I valori dell'ascissa devono seguire una serie geometrica[^1], nell'intervallo dei valori indicati prima.

> [!idea] 
> Si può fare ausilio di un `{python}for i in range(0,100)` e definire, la lunghezza $n$ dell'array come funzione esponenziale di $i$.

> [!example] 
> $$ n_{i} = \lfloor A\cdot B^{i} \rfloor $$
> dove $A,B$ sono costanti in virgola mobile calcolate opportunamente in modo da ottenere $n_{1}=100$, $n_{99}=100k$

#### Come trovare le costanti

```
n0   : 100
n1   : 1000
n2   : 10000
n3   : 100000
n4   : 1000000
...
n99  : 100000
```

troviamo $B$

$$
\begin{cases}
100'000=A\cdot B^{99} \\
100 = A\cdot B^{0}
\end{cases}
$$
troviamo $A=100$
$$
100000=100\cdot B^{99}
$$
$$
B^{99}=1000
$$
$$
B=\sqrt[99]{  1000}\approx 1.07
$$

```python
import math
A = 100
B = 1000 ** (1 / 99)
for i in range(100):
    print(math.floor(A * B ** i))
```






### Cosa cronometrare?

Ad un certo punto del codice avremo a disposizione un valore $n$ (lunghezza array) e $m$ (range di valori) quello che bisogna andare a fare è:
1. generare un array lungo $n$ con valori $[10,m]$
2. Il tempo dedicato all'inizializzazione dell'array può essere inclusa nella stima del tempo di esecuzione, oppure stimata separatamente e in seguito sottratta al tempo totale richiesto per l'inizializzazione e l'esecuzione di un algoritmo di ordinamento.
3. per ottenere stime più accurate è possibile eseguire il test per certi $m,n$ una decina di volte e poi calcolare la media (in questo modo la stima sarà meno sensibile al contenuto dell'array)

> [!note] 
> Curioso è provare a cronometrare anche il comportamento degli algoritmi nel loro caso migliore / peggiore

### Come cronometrare?

> [!note] 
> La stima dei tempi di esecuzione deve garantire un errore relativo massimo pari a $0.001$.

per cronometrare dobbiamo per prima cosa stimare la "**risoluzione**" del clock di sistema, per calcolare l'intervallo minimo di tempo misurabile:

```python
import time
...
def resolution():
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    stop = time.perf_counter()
    return stop - start
```

la risoluzione così stimata prende il nome di $R$, e con questa insieme all'errore massimo ammissibile $E=0.001$ possiamo calcolare il **tempo minimo misurabile**
$$
T_\text{min}=R\cdot\left( \frac{1}{E}+1 \right)
$$

Per stimare il tempo medio di esecuzione di un algoritmo, si utilizza un while, iterando l'esecuzione dell'algoritmi su un input di dimensione $n$, e misurando complessivamente un intervallo di tempo superiore a $T_\text{min}$. La misurazione deve essere effettuata *senza interrompere il clock*.

Il tempo medio di esecuzione per una singola istanza di input sarà quindi ottenuto calcolando il rapporto fra il tempo totale misurato e il numero di iterazioni dell'algoritmo eseguite (questa divisione non influisce sull'errore relativo commesso). La procedura di misurazione sarà quindi:

```python
def measure(n, m, min_time): 
	# n is the desired size of the array
	# m is the size of the range of integers appearing in the array    
	# min_time is the minumum measurable time, calculated as suggested above    
	count = 0    
	start_time = get_time()    
	while True:        
		a = initialize_array(n, m)
		execute_algorithm(a)
		count = count + 1
		end_time = get_time()
		if end_time - start_time >= min_time:
			break    
		return (end_time - start_time) / count
```

> [!note] 
> Qualora si desiderasse scomputare il tempo dedicato all'inizializzazione dell'input, è possibile stimare preventivamente il tempo medio di inizializzazione e in seguito sottrarre tale stima al tempo totale, ad esempio:
> 
> ```python
> def measure(n, m, min_time): 
> 	# n is the desired size of the array
> 	# m is the size of the range of integers appearing in the array    
> 	# min_time is the minumum measurable time, calculated as suggested above    
> 	start_time = get_time()    
> 	for i in range(0,10):	
> 		a = initialize_array(n, m)
> 	end_time = get_time()
> 	avg_init_time = (end_time - start_time) / 10
> 	
> 	count = 0    
> 	start_time = get_time()    
> 	while True:        
> 		a = initialize_array(n, m)
> 		execute_algorithm(a)
> 		count = count + 1
> 		end_time = get_time()
> 		if end_time - start_time >= min_time:
> 			break    
> 		return (end_time - start_time) / count - avg_init_time
> ```

> [!warning] 
> Nel caso si utilizzi il linguaggio di programmazione Python o Java, occorre prestare attenzione a non allocare ripetutamente grandi strutture dati (esempio, array o stringhe) in modo dinamico (ad esempio, con l'istruzione _new_). Tale pratica potrebbe esaurire in breve tempo la memoria RAM disponibile e attivare il _garbage collector_, creando picchi nei tempi di esecuzione misurati. Considerazioni simili si applicano anche ai linguaggi C e C++, che tuttavia permettono di gestire in modo esplicito l'allocazione e la liberazione della memoria.

> [!note] 
> Per effettuare tutte le misurazioni con precisione ragionevole non è necessario lasciare il pc eseguire per ore il codice! 
> Una decina di minuti (massimo un'ora) è ampiamente sufficiente a generare tutti i campioni e ad effettuare le misurazioni richieste. Nella fase di implementazione si consiglia di diminuire opportunamente i parametri (e.g. numero e range dei campioni) in modo da poter testare in pochi minutii il codice per le misurazioni

### Relazione

I dati raccolti devono essere presentati e discussi in una breve relazione (pdf) da caricare su e-learning.

(qualche decina di pagine è più che sufficiente)

> [!tip] 
> Si consiglia l'uso di grafici comparativi, sia in scale lineari - che riportano ad esempio $n$ in ascissa e $t(n)$ in ordinata - sia in scale doppiamente logaritmiche - che riportano ad esempio $\log(n)$ in ascissa e $\log(t(n))$ in ordinata

> [!note] 
> Il progetto viene considerato consegnato quando la relazione pdf viene caricata.

> [!note] 
> Consigliabile scegliere un rappresentante che caricherà i file sul sito + la relazione finale.
> 
> È IMPORTANTE CHE NELLA RELAZIONE CI SIANO I NOMI COGNOMI MAIL E NUMERI DI MATRICOLA DI OGNI COMPONENTE DEL GRUPPO




---

[^1]: giustamente dico io, non possiamo mica fare 10 elementi, 20, 30, ..., 100k elementi, non finiamo più
