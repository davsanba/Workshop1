import random
import sys


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
        print self.size
        for i in range(0, self.size):
            key_proto[i] = self.rdnGenerator()
        return key_proto

    def getKey(self):
        if self.key == None:
            key_proto = self.keyGen()
            print key_proto

new = KeyGenerator(4)
new.getKey()