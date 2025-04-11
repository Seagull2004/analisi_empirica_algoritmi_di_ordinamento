import matplotlib.pyplot as plt
import utils.geometricRangeGenerator as generator
import numpy as np

x = generator.generateGeometricRange(100, 100000, 100)
y = np.log(x)

plt.loglog(x, y, marker='o', linestyle='', color='red', markersize=2)
plt.title('Tempi di esecuzione')
plt.xlabel('Numero di elementi')
plt.ylabel('Tempo di esecuzione (s)')
plt.show()

