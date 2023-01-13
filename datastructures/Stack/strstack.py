from collections import deque

class Stack:
    def __init__(self):
        # self.container = arr.array('i', [])   
        # self.container = [] 
        self.container = deque()
        
    def push(self,item):        
        self.container.append(item)
    
    def pop(self):
        if(self.is_empty()):
            print("Error: empty stack.")
            return 
        return self.container.pop()
    
    def peek(self):
        if(self.is_empty()):
            print("Error: empty stack.")
            return 
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def is_full(self):
        return len(self.container) != 0
    
    def size(self):
        return len(self.container)
    
    def show(self):
        print(self.container)
        
        
def reverse_string(str):
    stack = Stack()
    stack = str.split()
    
    stack.show()                  
        
        
    
    return reversed

print(reverse_string("COVID-19"))
    
    
    