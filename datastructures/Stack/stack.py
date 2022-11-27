from collections import deque
import array as arr

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
    
s = Stack()

print(s.is_empty())
s.pop()
s.push(12)
print('after inserting 12, size=',s.size())

s.push(304)
print('after inserting 304, size=',s.size())

print('peek:',s.peek())

s.pop()

print('after pop peek:',s.peek())
print('after popping, size=',s.size())

s.push(5184)

print(s.peek())
print('is empty? ',s.is_empty())

print('is full? ',s.is_full())
