def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100  


print(ord('m'))
print(ord('a'))
print(get_hash('march 28'))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()

print(t.get_hash('march 6'))
print(t.get_hash('december 17'))

print(t.__setitem__('march 6',130))
print(t.__setitem__('march 1',20))
print(t.__setitem__('december 17',30))


print(t.arr) 
print(t.__getitem__('march 6'))

