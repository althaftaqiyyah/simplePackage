class Calculator():
    def __init__(self):
        pass

    def penjumlahan(self, a, b):
        return a+b

    def pengurangan(self, a, b):
        return a-b

    def perkalian(self, a, b):
        return a*b

    def pembagian(self, a, b):
        if b == 0:
            return 0
        else:
            return a/b
