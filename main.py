import algoritmi.countingSort as CS
import algoritmi.quicksort3Way as QS3
import algoritmi.quicksort as QS
import algoritmi.radixSort as RS
import utils.randomGenerator as generator
from utils.randomGenerator import Disposition
import utils.measurement as measurement
import utils.geometricRangeGenerator as generatorRange

for i in generatorRange.generateGeometricRange(100, 100000, 100):
    measurement.measureMeanTimeAlgo(CS.uniformedCountingSort, i, i)




