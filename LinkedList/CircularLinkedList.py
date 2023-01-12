class Node(object):
    
    def __init__(self, info = None, next_node = None):
        self.info = info
        self.next = next_node
        
        
class CircularLinkedList(object):
    
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
        if self.head != None:
            aft_head = self.head.next
            self.tail.next = aft_head
            self.head = aft_head
            
        else:
            raise ValueError("The list is empty")
        
    def deleteFromTail(self):
        if self.tail != None:
            curr_node = self.head
            while curr_node.next.next != self.head:                        
                curr_node = curr_node.next
             
            self.tail = curr_node
            
            curr_node.next = self.head
            
        else:
            raise ValueError("The list is empty")
        
        
        
cs = CircularLinkedList()
cs.new()
print(cs.isEmpty())
cs.addToHead(2)
cs.addToHead(1)
cs.addToTail(4)
cs.addToTail(75)
print(cs.toString())
cs.deleteFromHead()
print(cs.toString())
print(cs.find(4))
print(cs.isEmpty())
cs.deleteFromTail()
cs.deleteFromHead()
print(cs.toString())