import random

alphabet = "bcdfghjkmnpqrstvwxyz23456789BCDFGHJKMNPQRSTVWXYZ" # 46

class Service:
    def __init__(self, repository):
        self.repository = repository

    def create(self, value):
        n = self.repository.count()
        key = self.encode(n)
        self.customCreate(key, value)
        return key

    def customCreate(self, key, value):
        self.repository.set(key, value)
        return key

    def get(self, key):
        return self.repository.get(key)

    def encode(self, n):
        key = ""
        if n == 0 : key = alphabet[0]

        while n >= 1:
            alphLen = len(alphabet)
            key += alphabet[n % alphLen]
            n = n / alphLen

        shuffled = list(key)
        random.shuffle(shuffled)
        shuffled = "".join(shuffled)
        return shuffled
