class hashtable():
    def __init__(self, m):
        self.capacity = m
        self.table = [None]*m
        
    def find_hash(self, x):
        hash_ = x % self.capacity
        i = 0
        while self.table[hash_] is not None:
            i += 1
            hash_ = self.find_hash(x+i)
            
        return hash_
        
    def insert(self, x):
        hash_ = self.find_hash(x)
        
        self.table[hash_] = x
        
        return
    
    def search(self, x):
        hash_ = self.find_hash(x)
        
        return True
        
        
    def delete(self, x):
        hash_ = self.find_hash(x)
        self.table[hash_] = None
        
        return True
    
    def dump(self):
        for i in range(self.capacity):
            print('{} :'.format(i), end = ' ')
            print('{}'.format(self.table[i]))
            print('\n')
