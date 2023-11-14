import numpy as np

class DCT:
    def __init__(self):
        pass

    def dct_1D(self, vector):
        N = len(vector)
        X = np.array([np.cos(np.pi * u * (2 * x + 1) / (2 * N)) for u in range(N) for x in range(N)]).reshape(N, N)
        return X.dot(vector)
    
    def idct_1D(self, vector):
        N = len(vector)
        X = np.array([np.cos(np.pi * x * (2 * u + 1) / (2 * N)) for x in range(N) for u in range(N)]).reshape(N, N)
        return X.dot(vector) / N
    
    def dct_2D(self, matrix):
        return self.dct_1D(self.dct_1D(matrix).T).T
    
    def idct_2D(self, matrix):
        return self.idct_1D(self.idct_1D(matrix).T).T
    


# Example usage:
dct_processor = DCT()

# 1D Example
vector = np.array([4, 3, 2, 1, 0, -1, -2, -3])
dct_vector = dct_processor.dct_1D(vector)
idct_vector = dct_processor.idct_1D(dct_vector)
print("1D DCT:", dct_vector)
print("1D IDCT:", idct_vector)

# 2D Example
matrix = np.array([[255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255],
                   [255, 255, 255, 255, 255, 255, 255, 255]])

dct_matrix = dct_processor.dct_2D(matrix)
idct_matrix = dct_processor.idct_2D(dct_matrix)
print("2D DCT:")
print(dct_matrix)
print("2D IDCT:")
print(idct_matrix)