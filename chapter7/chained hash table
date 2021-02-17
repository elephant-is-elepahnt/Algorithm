class node():
    def __init__(self, value):
        self.hash = None
        self.value = value
        self.next = None
        
class hashtable():
    def __init__(self, m):
        self.capacity = m
        self.table = [None]*m
        
    def find_hash(self, x):
        hash_ = x % self.capacity
        return hash_
        
    def insert(self, x):
        hash_ = self.find_hash(x)
        a = node(x)
        a.hash = hash_
        if self.table[hash_] is None:
            self.table[hash_] = a
        else:
            a.next = self.table[hash_]
            self.table[hash_] = a
    
    def search(self, x):
        hash_ = self.find_hash(x)
        
        if self.table[hash_] is None:
            return False, False
        else:
            p = None
            a = self.table[hash_]
            while a.next is not None and a.value != x:
                p = a
                a = a.next
            
            return a, p
        
    def delete(self, x):
        a, p = self.search(x)
        if a == False:
            return False
        else:
            #if a is last
            if a.next is None:
                p.next = None
            #if a is first
            if p is None:
                self.table[self.find_hash(x)] = a.next
            else:
                p.next = a.next
        
        return True           
    
    def dump(self):
        for i in range(self.capacity):
            print('{} :'.format(i), end = ' ')
            a = self.table[i]            
            while a is not None:
                if a.next is None:
                    print('{}'.format(a.value), end = ' ')
                else:
                    print('{} ->'.format(a.value), end = ' ')
                a = a.next
            print('\n')
