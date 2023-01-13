import string 

class Stack:
    stack = []
    max_size = 0
    top = -1

    def __init__(self):
        pass

    def new(self, maximum):
        self.max_size = maximum
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def push(self, val):
        if not self.is_full():
            self.stack.append(val)
        else:
            pass

    def pop(self):
        if self.is_empty():
            return
        return self.stack.pop()
    
    def peek(self):
        if(self.is_empty()):
            # print("Error: empty stack.")
            return 
        return self.stack[-1]

    def clear(self):
        while not self.is_empty():
            self.stack.pop()
            
    def show(self):
        print(self.stack)
            


def is_operand(c):
    operands = list(string.ascii_letters)
    return c in operands

def is_operator(c):
    operators = "+-*/^"
    return c in operators

def get_precedence(c):
    pre = 0
    
    if (c == '^'):
        pre = 3
    elif(c == '/' or c == '*'):
        pre = 2
    elif(c == '+' or c == '-'):
        pre = 1
        
    return pre 


def reverse(infix):
    rev = ""
    for ch in infix[::-1]:
        if ch==')':
            rev+='('
        elif ch=='(':
            rev+=')'
        else:
            rev+=ch
    return rev

def infix_to_prefix(exp):
    result = ""
    rev = reverse(exp)
    
    s = Stack()    
    s.new(100)
    
    for ch in rev:
        if is_operand(ch):
            result += ch
        elif is_operator(ch): 
            chPre = get_precedence(ch)                  
            if s.is_empty():
                s.push(ch)
            else:
                while True:      
                    peekPre = get_precedence(s.peek())          
                    if peekPre >= chPre:
                        spop = s.pop()
                        result += spop
                    else:
                        s.push(ch)
                        break
        elif ch == '(':      
            s.push(ch)
        elif ch == ')':
            while True:        
                if s.peek() == '(':
                    s.pop()
                    break
                else:
                    result += s.pop()   
                    
    while not s.is_empty():
        result += s.pop()   
        
    return reverse(result)


print(infix_to_prefix("a+b*c"))         # +a*bc
print(infix_to_prefix("a*(b+c)"))       # *a+bc
print(infix_to_prefix("a/b+c/d"))       # +/ab/cd
print(infix_to_prefix("(a+b)*(c+d)"))   #*+ab+cd

