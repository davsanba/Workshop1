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
"""
import pandas as pd
import numpy as np # Only necessary for this example if you don't use it no poblem

# Random data
my_dataframe = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])

import matplotlib.pyplot as plt
from pandas.tools.plotting import table

ax = plt.subplot(121) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

table(ax, my_dataframe)  # where df is your data frame

plt.savefig('mytable.png')
"""