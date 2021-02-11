class RBT:
    def __init__(self):
        self.root = None
        self.NIL = Node(None, None, 'BLACK')
        
    def rotate_left(self, p):
        x = p.right
        
        #x의 왼쪽 서브트리를 p에 달아줌
        p.right = x.left
        if x.left != self.NIL:
            x.left.parent = p
        
        #옮겨진 x의 parent를 다시 복구
        if x != self.NIL:
            x.parent = p.parent
        if p.parent is not None:
            if p.parent.left == p:
                p.parent.left = x
            else:
                p.parent.right = x
        else:
            self.root = x
        
        #x와 p를 연결
        x.left = p
        if p != self.NIL:
            p.parent = x
        
            
    #p는 회전 축        
    def rotate_right(self, p):
        x = p.left
        
        #축이 오른쪽으로 이동
        p.left = x.right
        if x.right != self.NIL:
            x.right.parent = p
        
        
        #x의 부모 관계 형성
        if x != self.NIL:
            x.parent = p.parent
        if p.parent is not None:
            if p.parent.left == p:
                p.parent.left = x
            else:
                p.parent.right = x
        #p가 root였음
        else:
            self.root = x
        
        #p와 x 관계형성
        x.right = p
        if x != self.NIL:
            p.parent = x
            
        
        
        
    def fix_insert(self, x):
        #x의 부모가 black이면 그냥 삽입 끝 -> red일때가 문제
        while x != self.root and x.parent.color == 'RED':
            # p :부모 노드, pp : 조부모 노드, s : 삼촌 노드
            pp = x.parent.parent
            p = x.parent
            if pp.left == p:
                s = pp.right
            else:
                s = pp.left
                
            #case 1
            if s.color == 'RED':
                p.color = 'BLACK'
                pp.color = 'RED'
                s.color = 'BLACK'
                x = pp
                
            #case2 -> 삼촌이 black
            else:
                #pp의 왼쪽 자식이 p
                if pp.left == p:
                    #case 2-1
                    if p.right == x:
                        x = x.parent
                        self.rotate_left(x)
                    
                    #case 2-2
                    #옮겨진 p와 pp의 색을 바꾼다.
                    x.parent.color = 'BLACK'
                    x.parent.parent.color = 'RED'
                    self.rotate_right(x.parent.parent)
                    
                #pp의 오른쪽 자식이 p
                else:
                    #case 2-1
                    if p.left == x:
                        x = p
                        self.rotate_right(x)
                    
                    
                    x.parent.color = 'BLACK'
                    x.parent.parent.color = 'RED'
                    self.rotate_left(x.parent.parent)
            
            self.root.color = 'BLACK'
                    
                    
                    
        
    def insert(self, key, value):
        x = Node(key, value)
        x.right = self.NIL
        x.left = self.NIL
        #들어갈 위치 찾기
        cur = self.root
        p = None
        if self.root is None:
            self.root = x
            self.root.color = 'BLACK'
            return x
        else:
            while cur != self.NIL:
                if cur.key == key:
                    return False
                else:
                    p = cur
                    if cur.key > key:
                        cur = cur.left
                    else:
                        cur = cur.right
        
        x.parent = p
        if p.key>x.key:
            p.left = x
        else:
            p.right = x
            
        #pp까지 있는지 확인
        if x.parent.parent is None:
            return x
        else: 
            self.fix_insert(x)
            return x
        
    def fix_delete(self, x):
        p = x.parent
        
        while x != self.root and x.color == 'BLACK':
            #x가 왼쪽 서브 트리일때
            if p.left == x:
                #삼촌과 삼촌 자식들을 구한다.
                s = p.right
                l = s.left
                r = s.right

                #case 1-1
                if p.color == 'RED' and l.color == 'BLACK' and r.color == 'BLACK':
                        p.color = 'BLACK'
                        s.color = 'RED'
                        break
                
                #case *-2
                elif s.color == 'BLACK' and r.color == 'RED':
                    s.color = p.color
                    p.color = 'BLACK'
                    r.color = 'BLACK'
                    rotate_left(p)
                    break
                
                #case *-3
                elif s.color == 'BLACK' and l.color == 'RED' and r.color == 'BLACK':
                    l.color = 'BLACK'
                    s.color = 'RED'
                    rotate_right(s)
                
                #case 2-1
                elif s.color == 'BLACK' and l.color == 'BLACK' and r.color == 'BLACK':
                    s.color = 'RED'
                    x = p
                    
                #case 2-4
                else:
                    p.color = 'RED'
                    s.color = 'BLACK'
                    rotate_left(p)
                    
            
            else:
                #삼촌과 삼촌 자식들을 구한다.
                s = p.right
                l = s.left
                r = s.right
                
                #case 1-1
                if p.color == 'RED' and l.color == 'BLACK' and r.color == 'BLACK':
                    p.color = 'BLACK'
                    s.color = 'RED'
                    break
                
                #case *-2
                elif s.color == 'BLACK' and l.color == 'RED':
                    s.color = p.color
                    p.color = 'BLACK'
                    rotate_right(p)
                    break
                    
                #case *-3
                elif s.color == 'BLACK' and r.color == 'RED' and l.color == 'BLACK':
                    s.color = r.color
                    r.color = 'BLACK'
                    rotate_left(s)
                
                #case 2-1
                elif s.color == 'BLACK' and r.color == 'BLACK' and l.color == 'BLACK':
                    s.color = 'RED'
                    x = p
                    
                #case 2-4
                else:
                    p.color = s.color
                    s.color = 'BLACK'
                    rotate_right(p)
                    
        x.color = 'BLACK'
        
        
    def delete(self, key):
        p = None
        cur = self.root
        cur_is_left = True
        #삭제할 곳 찾기
        while cur != self.NIL:
            if cur.key == key:
                break
            else:
                p = cur
                if cur.key > key:
                    cur = cur.left
                else:
                    cur = cur.right
            if cur == self.NIL:
                return False
        
        #successor 찾기(m)
        #만약 삭제할 노드의 오른쪽 또는 왼쪽이 NIL이면 그 다음 노드에 연결만 하면됨
        if cur.left == self.NIL or cur.right == self.NIL:
            m = cur
        else:
            #만약 삭제한 뒤에 채워 넣을 다음 노드를 찾는다
            m = cur.right
            while m.left != self.NIL:
                m = m.left
        
        #삭제할 노드의 다음 노드(m)의 다음 값을 찾는다
        if m.left != self.NIL:
            x = m.left
        else:
            x = m.right
        
        #x와 m의 부모를 잇는다.
        x.parent = m.parent
        if m.parent is not None:
            if m.parent.left == m:
                m.parent.left = x
            else:
                m.parent.right = x
        else:
            self.root = x
        
        #m과 cur이 같은 경우는 그냥 이으면 되는 것
        if m != cur:
            cur.key = m.key
            cur.value = m.value
        
        if m.color == 'RED':
            return True
        else:
            self.fix_delete(x)
        
            
        
        
        
                        
                
    
