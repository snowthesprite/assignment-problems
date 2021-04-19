class HashTable :
    def __init__(self, num_buckets) :
        self.mod = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]

    def hash_function(self, string) :
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        sum = 0
        for char in string :
            sum += alphabet.index(char)
        return sum % self.mod

    def insert(self, key, value) :
        index = self.hash_function(key)
        self.buckets[index].append((key, value))

    def find(self, key) :
        index = self.hash_function(key)
        for pair in self.buckets[index] :
            if pair[0] == key :
                return pair[1]