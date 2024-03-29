class Node:
    def __init__(self, el, p, n):
        self.info = el
        self.prev = p 
        self.next = n
    

class DoublyLinkedList:
    def __init__(self):  
        pass
    
    def new(self):
        self.head = None
        self.tail = None
        return self

    def isEmpty(self):
        return self.head == None
    
    def toString(self):
        if(self.head is None):
            raise Exception("Linkedlist is empty.")   
        
        p = self.head
        s = ''
        while p:
            s += str(p.info) + " "
            p = p.next
            
        return s
    
    def find(self, el):
        p = self.head
        
        while p != None and p.info != el:
            p = p.next
            
        return p
    
    def addToHead(self, el):
        if self.head == None:
            self.head = Node(el, None, None)
            self.tail = self.head
        
        else:
            self.head = Node(el, None, self.head)
            self.head.next.prev = self.head
            
    def addToTail(self, el):
        p = self.tail 
        node = Node(el, p, None)
        
        if self.tail  == None:
            self.tail = self.head = node
        else:
             self.tail = node
             p.next = self.tail
             p.next.prev = p
    
    def deleteFromHead(self):
        if self.isEmpty(): 
            raise Exception('LinkedList is empty.')
        
        p = self.head
        el = p.info
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = p.next
            self.head.next = p.next.next
            self.head.prev = None
            
            
        return el
    
    def deleteFromTail(self):
        if self.isEmpty():
            raise Exception("Linkedlist is empty.")

        d = self.tail
        el = d.info
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        return el
    
    def deleteElement(self, elem):
        if self.isEmpty(): 
            raise Exception('LinkedList is empty.')
        
        if elem == self.head.info:
            return self.deleteFromHead()
        
        if elem == self.tail.info:
            return self.deleteFromTail()
        
        pred = self.head
        t = self.head.next
        
        while t!=None and t.info!=elem:
            pred = pred.next
            t = t.next 
        
        if t==None:
            raise Exception('Element not found.')
        else:
            pred.next = t.next
            
        return elem
        
dlist = DoublyLinkedList()
dlist.new()
print(dlist.isEmpty())
dlist.addToHead(43)
dlist.addToHead(66)
dlist.addToTail(99)
dlist.addToTail(54)
dlist.deleteFromHead()
dlist.deleteFromTail()
print(dlist.toString())



