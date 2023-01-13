class Node:
    
    def __init__(self, info = None, next_node = None):
        self.info = info
        self.next = next_node
        
        
class CircularLinkedList:
    
    def __init__(self):
        pass
    
    def new(self):
        self.head = None
        self.tail = None
        return self
    
    def isEmpty(self):
        return self.head == None
    
    def find(self, el):
        p = self.head
        
        while p != None and p.info != el:
            p = p.next
        
        if p == None:
            return None
        
        return p
    
    def toString(self):        
        if(self.head is None):
            raise Exception("Linkedlist is empty.")  
        
        p = self.head
        s = ''
        
        while p:
            s += str(p.info) + " "
            p = p.next
            
            if p == self.head:
                break
        
        return s
    
    
    def addToTail(self, info):
        node = Node(info) 
        
        if self.head == None:            
            self.head = node
            self.head.next = node
            self.tail = node
            return
        
        else:
            self.tail.next = node
            node.next = self.head        
            self.tail = node
            return
                
            
    def addToHead(self, info):
        node = Node(info)
        node.next = self.head        
        curr_node = self.head
                   
        if curr_node == None:            
            self.head = node
            self.tail = node
            self.head.next = node
            return
        
        else:
            self.tail.next = node
            node.next = self.head        
            self.head = node
            return
    
    def deleteFromHead(self):        
        if self.isEmpty():
            raise ValueError("The list is empty")
        
        p = self.head.info
        
        if self.head == self.tail:
            self.head = self.tail = None
        else: 
            aft_head = self.head.next
            self.head = aft_head
            self.tail.next = aft_head
        
        return p
        
    def deleteFromTail(self):
        if self.isEmpty():
            raise ValueError("The list is empty")
        
        p = self.tail.info
        
        if self.head == self.tail:
            self.head = self.tail = None        
        else:
            curr_node = self.head
            while curr_node.next.next != self.head:                        
                curr_node = curr_node.next
             
            self.tail = curr_node
            
            curr_node.next = self.head
        
        return p
        
        
        
cs = CircularLinkedList()
cs.new()
print(cs.isEmpty())
cs.addToHead(2)
cs.addToHead(71)
# cs.addToTail(4)
# cs.addToTail(75)
print(cs.toString())
print("deleted ",cs.deleteFromHead())
print(cs.toString())
print("del",cs.deleteFromHead())
print(cs.toString())