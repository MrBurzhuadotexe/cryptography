from random import randint, getrandbits
from math import gcd as bltin_gcd
from sympy import isprime


def coprime(a, b):
    return bltin_gcd(a, b) == 1


class BBS:
    p = 0
    q = 0
    n = 0
    seed = 0
    generatedValues = []


    def __init__(self, p, q):
        if p > 0 and q > 0:
            if isprime(p) and isprime(q):
                self.p = p
                self.q = q
                self.__setN()
                self.__setSeed()
            else:
                raise Exception("Liczby nie są pierwsze")
        else:
            raise Exception("Liczby nie są pozytywne")


    def __setN(self):
        self.n = self.p * self.q


    def __setSeed(self):
        while not coprime(self.n, self.seed) and self.seed < 1:
            self.seed = randint(0, self.n - 1)


    def __generateValue(self):
        if self.p > 0 and self.q > 0:
            x = 0
            while not coprime(self.n, x):
                x = randint(0, self.n)
            return pow(x, 2) % self.n


    def create_sequance(self, amount):
        if self.p == self.q:
            raise Exception("liczby p i q muszą być różne")

        else:
            arr = []
            amount += 1

            for i in range(amount):
                generatedValue = self.__generateValue()
                self.generatedValues.append(generatedValue)

                if generatedValue % 2 == 0:
                    arr.append(0)
                else:
                    arr.append(1)

            return arr
