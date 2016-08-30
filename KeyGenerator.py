class KeyGenerator:
    def __init__(self, textLen):
        self.size = (textLen^2)/4

    def generator(self):
