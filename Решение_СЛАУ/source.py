
import numpy as np
arr = np.linalg.solve([[0.,2.,3.],
                [1.,2.,4.],
                [4.,5.,6.]],[13.,17.,32.])
print(arr.tolist())