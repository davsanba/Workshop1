import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.matrix.__str__()

    def rotate90(self):
        new_matrix = self.matrix
        new_matrix = new_matrix.transpose()
        for i in range(0, new_matrix.shape[0]):
            new_matrix[i] = np.fliplr(new_matrix[i])
        self.matrix = new_matrix
        return self.matrix
#print matrix

#print matrix.rotate90()

