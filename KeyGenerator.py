import random
import sys
from math import ceil, sqrt
from itertools import repeat
import numpy as np
import random
from MatrixRotator import Matrix


class KeyGenerator:
    def __init__(self, textLen):
        self.len = textLen
        self.size = (textLen*textLen)/4
        self.key = None

    def rdnGenerator(self):
        rnd = random.SystemRandom()
        return rnd.randint(0, self.len), rnd.randint(0, self.len)

    def keyGen(self):
        key_proto = [None]*self.size
        for i in range(0, self.size):
            key_proto[i] = self.rdnGenerator()
        return key_proto

    def getKey(self):
        if self.key == None:
            key_proto = self.keyGen()


def refill_input(input_string):
    list_input = list(input_string.upper())
    total_refill = check_size(input_string)**2 - len(list_input)
    return list_input + list(repeat("X", total_refill))

def check_size(input_string):
    len_key = int(ceil(sqrt(len(input_string))))
    if int(len_key) % 2 == 1:
        len_key += 1
    return len_key

def key_generator(input_string):
    # Length Key
    length_key = check_size(input_string)

    # Create a nxn grid where 'n' is even. In the following example n=6.
    # Divide this grid up into 4 sections of size n/2.
    grid_part = int(length_key/2)

    # Number each section
    numbers_cordenates = [np.arange(1, grid_part**2 + 1)]
    grid = np.array(numbers_cordenates)
    grid.shape = (grid_part, grid_part)

    # Rotating the numbering by 90 degrees in each section.
    initial_matrix = grid
    initial_matrix90 = np.rot90(grid)
    initial_matrix180 = np.rot90(grid,2)
    initial_matrix270 = np.rot90(grid,3)

    # Concatenate all sections
    first_part = np.concatenate((initial_matrix, initial_matrix90),axis=0)
    second_part = np.concatenate((initial_matrix270, initial_matrix180), axis=0)

    # Posible cordenates
    matrix = np.concatenate((first_part,second_part), axis=1)
    dict_all_cordenates = {}
    for i in xrange(len(numbers_cordenates[0])):
        dict_all_cordenates[numbers_cordenates[0][i]] = np.nonzero(matrix == int(i+1))

    # Convert cordenates into (x,y) values
    cordenates = {}
    for cord in dict_all_cordenates:
        cor_each_space = []
        for m,n in zip(dict_all_cordenates[cord][0], dict_all_cordenates[cord][1]):
            cor_each_space.append((m,n))
        cordenates[cord] =cor_each_space

    key_rows_cordenates = []
    key_cols_cordenates = []
    # through the matrix and choose a cordenate randomly
    for rn_cord in cordenates:
        my_random_cordinate = random.randrange(0, 4)
        key_rows_cordenates.append(cordenates[rn_cord][my_random_cordinate][0])
        key_cols_cordenates.append(cordenates[rn_cord][my_random_cordinate][1])

    # Finally the key
    key = np.zeros((int(length_key),int(length_key)))
    key[key_rows_cordenates, key_cols_cordenates] = 1
    return key

input_string = "IntroductionToCryptography"
# input_string = "Cryptography"

def fill_matrix(input_string):
    # Key
    key = key_generator(input_string)
    # String refilled
    string_to_cipher = refill_input(input_string)
    list_asci = [ord(s) for s in string_to_cipher]

    # Divide a list into n equal parts
    # Taken from: http://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
    div_list = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
    total_parts = div_list(list_asci,len(list_asci)/4)

    # Key strings
    key_ascii = np.copy(key)
    cordenates = np.nonzero(key == 1)
    key_ascii[cordenates] = total_parts[0]
    for part in range(1,len(total_parts)):
        key = np.rot90(key)
        key_ascii += key
        cordenates = np.nonzero(key_ascii == 1)
        key_ascii[cordenates] = total_parts[part]

    return key_ascii

print "Final Matrix"
print fill_matrix(input_string)


