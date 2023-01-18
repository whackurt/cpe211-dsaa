class Node:
    def __init__(self, el, next=None):        
        self.el = el
        self.next = next

class SinglyLinkedList:
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
            print("Linkedlist is empty.")
            return         
        
        p = self.head
        s = ''
        while p:
            s += str(p.el) + " "
            p = p.next
            
        return s
    
    def find(self, el):
        p = self.head
        
        while p != None and p.el != el:
            p = p.next
            
        return p
    
    def addToHead(self, el):
        node = Node(el, self.head)
        self.head = node
        
        if self.tail == None:
            self.tail = self.head

    def deleteFromHead(self):
        if self.isEmpty(): 
            raise Exception('LinkedList is empty.')
        
        p = self.head
        el = p.el
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            
        return el
    
    def deleteFromTail(self):
        if self.isEmpty(): 
            raise Exception('LinkedList is empty.')
        
        t = self.tail
        el = t.el
        
        if self.head == self.tail:
            self.head = self.tail = None
            
        else:
            p = self.head
            while p.next != t:
                p = p.next
            
            self.tail = p
            self.tail.next = None
            
        return el
    
    def deleteElement(self, elem):
        if self.isEmpty(): 
            raise Exception('LinkedList is empty.')
        
        if elem == self.head.el:
            return self.deleteFromHead()
        
        if elem == self.tail.el:
            return self.deleteFromTail()
        
        pred = self.head
        t = self.head.next
        
        while t!=None and t.el!=elem:
            pred = pred.next
            t = t.next 
        
        if t==None:
            raise Exception('Element not found.')
        else:
            pred.next = t.next
            
        return elem
        
# slist = SinglyLinkedList()
# slist.new()
# print(slist.isEmpty())
# slist.addToHead(7)
# slist.addToHead(12)
# slist.addToHead(43)
# print(slist.toString())
# print(slist.find(2))
# print("del",slist.deleteFromHead())
# print(slist.toString())
# slist.addToHead(98)
# slist.addToHead(116)
# print(slist.toString())
# print("deleted ",slist.deleteElement(21))
# print(slist.toString())


