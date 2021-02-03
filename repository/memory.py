class Storage:
    def __init__(self):
        self.memory = dict()

    def set(self, key, value): self.memory[key] = value
    def get(self, key): return self.memory[key]
    def count(self): return len(self.memory)
