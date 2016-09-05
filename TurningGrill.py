import sys
from math import ceil, sqrt
from itertools import repeat
import numpy as np
from PyQt4.QtGui import QTableWidgetItem

from KeyGenerator import KeyGenerator as keyg
from PyQt4 import QtCore, QtGui, uic
from Interface import *


class TurningGrill(QtGui.QMainWindow, Ui_TurningGrill):

    def __init__(self):
        self.rotation = "clockwise"
        super(self.__class__, self).__init__()
        self.ui = Ui_TurningGrill()
        self.ui.setupUi(self)
        self.ui.EncryptButton.clicked.connect(self.check_encrypt)
        self.ui.clockwiseButton.clicked.connect(lambda : self.set_rotation("clockwise"))
        self.ui.AnticlockwiseButton.clicked.connect(lambda : self.set_rotation("anticlockwise"))

    def check_encrypt(self):
        plain_text = self.ui.PlainText.toPlainText()
        if plain_text != "":
            matrix, key, len = self.encrypt_string(str(plain_text),self.rotation)
            self.ui.KeyShow.setPlainText(str(key))
            self.ui.TableSize.setValue(self.check_size(plain_text))
            self.print_matrix(matrix)

    def print_matrix(self, matrix):
        size = matrix.shape
        self.ui.Matrix.setRowCount(size[0])
        self.ui.Matrix.resizeRowsToContents()
        self.ui.Matrix.setColumnCount(size[1])
        self.ui.Matrix.resizeColumnsToContents()
        for i in range(0,size[0]):
            for j in range (0, size[1]):
                self.ui.Matrix.setItem(i,j, QTableWidgetItem(matrix[i][j]))

    def print_rotation_matrix(self, matrix, rotation):
        if rotation != 3:
            if rotation == 1: table = self.ui.Rotation2
            elif rotation == 2: table = self.ui.Rotation3
            else: table = self.ui.Rotation1

            size = matrix.shape
            table.setStyleSheet('font-size: 5pt')

            table.setRowCount(size[0])
            table.resizeRowsToContents()
            table.setColumnCount(size[1])
            table.resizeColumnsToContents()

            for i in range(0,size[0]):
                for j in range (0, size[1]):
                    table.setItem(i,j, QTableWidgetItem(matrix[i][j]))


    def set_rotation(self, rotation):
        self.rotation = rotation

    def refill_input(slef, input_string):
        list_input = list(input_string.upper())
        total_refill = slef.check_size(input_string) ** 2 - len(list_input)
        return list_input + list(repeat("X", total_refill))

    def check_size(self, input_string):
        len_key = int(ceil(sqrt(len(input_string))))
        if int(len_key) % 2 == 1:
            len_key += 1
        return len_key

    def encrypt_string(self,input_string,rotation):
        #fill string
        original_len = len(input_string)
        string_to_cipher = self.refill_input(input_string)
        string_len = self.check_size(string_to_cipher)

        # Key class
        key = keyg(string_len)

        list_ascii = [ord(s) for s in string_to_cipher]

        # Divide a list into n equal parts
        # Taken from: http://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
        div_list = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
        total_parts = div_list(string_to_cipher, len(string_to_cipher) / 4)

        cipher_matrix = np.chararray([string_len,string_len])

        # Key strings
        cipher_matrix[key.coordinates()] = total_parts[0]
        self.print_rotation_matrix(cipher_matrix,0)

        if rotation == "anticlockwise":
            for part in range(1, len(total_parts)):
                cipher_matrix = np.rot90(cipher_matrix)
                cipher_matrix[key.coordinates()] = total_parts[part]
                self.print_rotation_matrix(cipher_matrix, part)

        elif rotation == "clockwise":
            for part in range(1, len(total_parts)):
                cipher_matrix = np.rot90(cipher_matrix,3)
                cipher_matrix[key.coordinates()] = total_parts[part]
                self.print_rotation_matrix(cipher_matrix, part)
        else:
            "Wrong Rotation Input"

        return cipher_matrix, key, original_len

    def decrypt_string(self,cipher_matrix, key, original_len, rotation):

        original_string = []

        if rotation == "anticlockwise":
            for part in range(0, 4):
                text = cipher_matrix[key.coordinates()]
                cipher_matrix = np.rot90(cipher_matrix, 3)
                text = ls = [' ' if (x == '') else x for x in text]
                original_string.insert(0,''.join(text))
        elif rotation == "clockwise":
            for part in range(0, 4):
                text = cipher_matrix[key.coordinates()]
                cipher_matrix = np.rot90(cipher_matrix)
                text = ls = [' ' if (x == '') else x for x in text]
                original_string.insert(0,''.join(text))
        else:
            "Wrong Rotation Input"

        original_string = ''.join(original_string)
        return original_string[0:original_len]





if __name__ == '__main__':              # if we're running file directly and not importing it
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = TurningGrill()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
"""""
programa = TurningGrill()

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
rotation1 = "anticlockwise"
rotation2 = "clockwise"


matriz,key, len= programa.encrypt_string(string,rotation1)

print matriz

stringde = programa.decrypt_string(matriz, key, len, rotation1)
print stringde


"""
