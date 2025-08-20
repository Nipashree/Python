import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)
print("Original 4x4 Matrix:\n", matrix)

result = np.hstack((matrix[-2:, [0]], matrix[-2:, -2:]))
print("\nExtracted Elements:\n", result)
