class HashTable:
    def __init__(self, max=100) -> None:
        self.MAX = max
        self.arr = [[] for i in range(self.MAX)]  # list comprehension

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):  # https://docs.python.org/3/library/operator.html
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):  # https://docs.python.org/3/library/operator.html
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

if __name__ == '__main__':
    t = HashTable(10)
    t['march 6'] = 120
    t['march 6'] = 78
    t['march 8'] = 67
    t['march 9'] = 4
    t['march 17'] = 459
    
    print(t.arr)
    print(t['march 6'])
    print(t['march 17'])
    
    del t['march 6']
    print(t.arr)
    
    del t['march 17']
    print(t.arr)