class hashtable():
    def __init__(self, m):
        self.capacity = m
        self.table = [None]*m
        
    def find_hash(self, x):
        hash_ = x % self.capacity
        i = 0
        while self.table[hash_] is not None:
            i += 1
            hash_ = (x+i) % self.capacity
            
        return hash_
        
    def insert(self, x):
        hash_ = x % self.capacity
        i = 0
        while self.table[hash_] is not None and self.table[hash_] != 'DELETED':
            i += 1
            hash_ = (x+i) % self.capacity
        self.table[hash_] = x
        
        return
    
    def search_loc(self, x):
        hash_ = x % self.capacity
        i = 0
        if self.table[hash_] == x:
            return hash_
        
        while self.table[hash_] is not None:
            i += 1
            hash_ = (x+i) % self.capacity
            if self.table[hash_] == x:
                return hash_
            
        return False
        
        
    def delete(self, x):
        hash_ = self.search_loc(x)
        if hash_ != False:
            self.table[hash_] = 'DELETED'
        else:
            
            return False
    
    def dump(self):
        for i in range(self.capacity):
            print('{} :'.format(i), end = ' ')
            print('{}'.format(self.table[i]))
            print('\n')
