class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def search(self, x):
        #t is root of the Tree
        t = self.root       
        while True:
            if t is None:
                return None
            elif t.key == x:
                return t
            elif t.key > x:
                t = t.left
            else:
                t = t.right
        
        
    def treeInsert(self, x, value):
        #재귀를 위해 함수안에 또다른 함수를 넣는다. 
        def add_node(node:Node, key = x, value = value):
            if key == node.key:
                return False
            elif key <node.key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(x, value)
            return True
        else:
            return add_node(self.root, x, value)
                 
            
    def treeDelete(self, key):
        cur = self.root
        parent_node = None
        cur_is_left = True
        #삭제할 노드 찾기
        while True:
            if cur is None:
                return False
            
            if cur.key == key:
                break
            
            else:
                if cur.key > key:
                    parent_node = cur
                    cur = cur.left
                    cur_is_left = True
                else:
                    parent_node = cur
                    cur = cur.right
                    cur_is_left = False
        print(cur_is_left)            
        remove_node = cur
        remove_parent = parent_node
        #removal 1
        if remove_node.left is None and remove_node.right is None:
            if cur_is_left is True:
                remove_parent.left = None
            else:
                remove_parent.right = None
            return True
        
        #removal 2
        if remove_node.left is None and remove_node.right is not None:
            if cur_is_left is True:
                remove_parent.left = remove_node.right
            else:
                remove_parent.right = remove_node.right
            return True
        elif remove_node.left is not None and remove_node.right is None:
            if cur_is_left is True:
                remove_parent.left = remove_node.left
            else:
                remove_parent.right = remove_node.left
            return True
        
        #removal 3
        else:
            temp = remove_node.right
            while temp.left is not None:
                remove_parent = temp
                temp = temp.left
            #key change
            remove_node.key, remove_node.value = temp.key, temp.value
            #remove
            if remove_node.right == temp:
                remove_node.right = temp.right
            else:
                remove_parent.left = temp.right
                
        return True
            
        
                
            
                
            
            
