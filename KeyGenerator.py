import numpy as np
import random

# Class to generate the random key
class KeyGenerator:
    # Initialization
    def __init__(self, len_key):
        self.key = []
        self.len = len_key
        self.key_generator

    # Key length
    def __len__(self):
        return len(self.key)

    ##############################
    # Key random generator
    ##############################
    @property
    def key_generator(self):
        # Length Key
        length_key = self.len

        # Create a nxn grid where 'n' is even. In the following example n=6.
        # Divide this grid up into 4 sections of size n/2.
        grid_part = int(length_key / 2)

        # Number each section
        numbers_cordenates = [np.arange(1, grid_part ** 2 + 1)]
        grid = np.array(numbers_cordenates)
        grid.shape = (grid_part, grid_part)

        # Rotating the numbering by 90 degrees in each section.
        initial_matrix = grid
        initial_matrix90 = np.rot90(grid)
        initial_matrix180 = np.rot90(grid, 2)
        initial_matrix270 = np.rot90(grid, 3)

        # Concatenate all sections
        first_part = np.concatenate((initial_matrix, initial_matrix90), axis=0)
        second_part = np.concatenate((initial_matrix270, initial_matrix180), axis=0)

        # Posible cordenates
        matrix = np.concatenate((first_part, second_part), axis=1)
        dict_all_cordenates = {}
        for i in xrange(len(numbers_cordenates[0])):
            dict_all_cordenates[numbers_cordenates[0][i]] = np.nonzero(matrix == int(i + 1))

        # Convert cordenates into (x,y) values
        cordenates = {}
        for cord in dict_all_cordenates:
            cor_each_space = []
            for m, n in zip(dict_all_cordenates[cord][0], dict_all_cordenates[cord][1]):
                cor_each_space.append((m, n))
            cordenates[cord] = cor_each_space

        key_rows_cordenates = []
        key_cols_cordenates = []
        # through the matrix and choose a cordenate randomly
        for rn_cord in cordenates:
            my_random_cordinate = random.randrange(0, 4)
            key_rows_cordenates.append(cordenates[rn_cord][my_random_cordinate][0])
            key_cols_cordenates.append(cordenates[rn_cord][my_random_cordinate][1])
        self.key = zip(key_rows_cordenates, key_cols_cordenates)
        self.key.sort()

    # To string method
    def __str__(self):
        return self.key.__str__()

    # x,y positions for the key
    def x(self, position):
        return self.key[position][0]
    def y(self, position):
        return self.key[position][1]

    # coordinates (x,y)
    def coordinates(self):
        return zip(*self.key)

    # KEY
    def key(self):
        return self.key

