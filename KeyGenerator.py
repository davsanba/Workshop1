import random
import sys


class KeyGenerator:
    def __init__(self, textLen):
        self.len = textLen
        self.size = (textLen^2)/4

    def generator(self):
        rnd = random.SystemRandom()
        return rnd.randint(0, self.len), rnd.randint(0, self.len)

    

new = KeyGenerator(4)

print new.generator()