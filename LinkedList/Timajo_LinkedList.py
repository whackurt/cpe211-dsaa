# Timajo, Kurt Vincent 
# CpE-2B
# # # # # # # # # # # # # # 
#     Singly Linked List  #
# # # # # # # # # # # # # #
class SNode:
    def __init__(self, el, next=None):        
        self.info = el
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
            s += str(p.info) + " -> "
            p = p.next
            
        return s
    
    def find(self, el):
        p = self.head
        
        while p != None and p.info != el:
            p = p.next
            
        return p
    
    def addToHead(self, el):
        node = SNode(el, self.head)
        self.head = node
        
        if self.tail == None:
            self.tail = self.head
            
    def addToTail(self, el):
        node = SNode(el)
        
        if self.head is None:
            self.head = self.tail = node 
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def deleteFromHead(self):
        if self.isEmpty(): 
            print('LinkedList is empty.')
            return 
        
        p = self.head
        el = p.info
            
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            
        return el
    
    def deleteFromTail(self):
        if self.isEmpty(): 
            print('LinkedList is empty.')
            return
        
        t = self.tail
        el = t.info
        
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
            print('LinkedList is empty.')
            return 
        
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
            print('Element not found.')
            return 
        else:
            pred.next = t.next
            
        return elem
  
    
# # # # # # # # # # # # # #
#   Doubly Linked List    #
# # # # # # # # # # # # # #
class DNode:
    def __init__(self, el, p, n):
        self.info = el
        self.prev = p 
        self.next = n
    
# inherited SinglyLinkedList because they have the 
# same methods except for adding and deleting info
class DoublyLinkedList(SinglyLinkedList): 
    def __init__(self):  
        pass
    
    def addToHead(self, el):
        if self.head == None:
            self.head = DNode(el, None, None)
            self.tail = self.head
        
        else:
            self.head = DNode(el, None, self.head)
            self.head.next.prev = self.head
    
    def addToTail(self, el):
        p = self.tail 
        node = DNode(el, p, None)
        
        if self.tail  == None:
            self.tail = self.head = node
        else:
             self.tail = node
             p.next = self.tail
             p.next.prev = p
    
    def deleteFromHead(self):
        if self.isEmpty(): 
            print('LinkedList is empty.')
            return 
        
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
            print("Linkedlist is empty.")
            return 

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
            print('LinkedList is empty.')
            return 
        
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
            print('Element not found.')
            return 
        else:
            pred.next = t.next
            
        return elem
        

# # # # # # # # # # # # # 
# Circular Linked List  #
# # # # # # # # # # # # #
class CNode:
    
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
            print("Linkedlist is empty.")   
            return 
           
        p = self.head
        s = ''
        
        while p:
            s += str(p.info) + " -> "
            p = p.next
            
            if p == self.head:
                break
        
        return s
    
    
    def addToTail(self, info):
        node = CNode(info) 
        
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
        node = CNode(info)
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
            print("The list is empty")
            return 
        
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
            print("The list is empty")
            return 
        
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


def choices():
    print("""
    a - isEmpty
    b - toString
    c - find
    d - addToHead
    e - addToTail
    f - deleteFromHead
    g - deleteFromTail
    h - deleteElement
    x - Back to Menu
            """)

def singlyOperations():
    print("\n\nSingly Linked List Implementation")
    slist = SinglyLinkedList()
    slist.new()
    print('A new Singly Linked List is created')
    
    op = ' '
    
    while op != 'x':
        choices()
        
        if op == 'a':
            print("isEmpty = ", slist.isEmpty())
        
        elif op == 'b':
            if slist.toString() == None:
                print('Linked list is empty.')

        elif op == 'c':
            el = input('Input element to find >> ')
            print(slist.find(el))
        
        elif op == 'd':
            el = input('Input element to add as head>> ')
            slist.addToHead(el)
            
        elif op == 'e':
            el = input('Input element to add as tail >> ')
            slist.addToTail(el)
            
        elif op == 'f':
            deleted = slist.deleteFromHead()
            if deleted:
                print("Deleted " + str(deleted) + " from head.")
            
        elif op == 'g':
            deleted = slist.deleteFromTail()
            if deleted:
                print("Deleted " + str(deleted) + " from tail.")
            
        elif op == 'h':
            el = input('Input element to delete >> ')
            deleted = slist.deleteElement(el)
            
            if deleted:
                print("Deleted " + str(deleted) + " from the list.")
        
        print(slist.toString()) if not slist.isEmpty() else None
        op = input('>> ')
        
    app()
    
    
def doublyOperations():
    print("\nDoubly Linked List Implementation")
    dlist = DoublyLinkedList()
    dlist.new()
    print('A new Doubly Linked List is created')
    
    op = ' '
    
    while op != 'x':
        choices()
        
        if op == 'a':
            print("isEmpty = ", dlist.isEmpty())
        
        elif op == 'b':
            if dlist.toString() == None:
                print('Linked list is empty.')

        elif op == 'c':
            el = input('Input element to find >> ')
            print(dlist.find(el))
        
        elif op == 'd':
            el = input('Input element to add >> ')
            dlist.addToHead(el)
            
        elif op == 'e':
            el = input('Input element to add as tail >> ')
            dlist.addToTail(el)
            
        elif op == 'f':
            deleted = dlist.deleteFromHead()
            if deleted:
                print("Deleted " + str(deleted) + " from head.")
            
        elif op == 'g':
            deleted = dlist.deleteFromTail()
            if deleted:
                print("Deleted " + str(deleted) + " from tail.")
            
        elif op == 'h':
            el = input('Input element to delete >> ')
            deleted = dlist.deleteElement(el)
            
            if deleted:
                print("Deleted " + str(deleted) + " from the list.")
        
        print(dlist.toString()) if not dlist.isEmpty() else None
        op = input('>> ')
        
        
    app()
        

def circularOperations():
    print("\nCircular Linked List Implementation")
    clist = CircularLinkedList()
    clist.new()
    print('A new Circular Linked List is created')

    op = ' '
    
    while op != 'x':
        print("""
    a - isEmpty
    b - toString
    c - find
    d - addToHead
    e - addToTail
    f - deleteFromHead
    g - deleteFromTail
    x - Back to Menu
            """)
        
        
        if op == 'a':
            print("isEmpty = ", clist.isEmpty())
        
        elif op == 'b':
            if clist.toString() == None:
                print('Linked list is empty.')
        
        elif op == 'c':
            el = input('Input element to find >> ')
            print(clist.find(el))
            
        elif op == 'd':
            el = input('Input element to add as head >> ')
            clist.addToHead(el)
            
        elif op == 'e':
            el = input('Input element to add as tail >> ')
            clist.addToTail(el)
            
        elif op == 'f':
            deleted = clist.deleteFromHead()
            if deleted:
                print("Deleted " + str(deleted) + " from tail.")
            
        elif op == 'g':
            deleted = clist.deleteFromTail()
            
            if deleted:
                print("Deleted " + str(deleted) + " from the list.")
        
        print(clist.toString()) if not clist.isEmpty() else None
        
        op = input('>> ')
        
    app()
    
    
def menu():
    ch = 0
    print("""
LinkedList Implementations
Select:
    (1) - Singly Linked List
    (2) - Doubly Linked List
    (3) - Circular Linked List
    
    (0) - Exit the program
          """)
    
    ch = int(input('>> '))
    return ch

def app():
    select = menu()
    print(select)
    if select == 1:
        singlyOperations()
        
    elif select == 2:
        doublyOperations()
    
    elif select == 3:
        circularOperations()
    
    elif select == 0:
        print("Terminating the program...")
        exit()
        
    else:
        app()
app()