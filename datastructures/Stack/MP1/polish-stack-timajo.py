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

# Machine Problem 1
def infix_to_postfix(infix):
    result = ""
    s = Stack()
    s.new(100)
    
    for ch in infix:
        # if operand, concat to result string
        if is_operand(ch): 
            result += ch
        elif is_operator(ch): 
            # if operator, get precedence
            chPre = get_precedence(ch)   
            
            # if stack is empty, directly push the ch to it                
            if s.is_empty():
                s.push(ch)
            # if stack isnt empty, check the precedence of the peek element   
                   
            else:
                # pop all elements while the precedence of the peek 
                # is greater or equal to the current character ch                  
                while True:      
                    peekPre = get_precedence(s.peek())          
                    if peekPre >= chPre:
                        spop = s.pop()
                        result += spop
                    else:
                        s.push(ch)
                        break
                    
        # if open parenthesis, push to stack
        elif ch == '(':      
            s.push(ch)
        # if close parenthesis, pop all elements until open parenthesis is the peek
        # pop the open parenthesis and stop popping
        elif ch == ')':
            while True:        
                if s.peek() == '(':
                    s.pop()
                    break
                else:
                    result += s.pop()   
    
    # if there is no more ch, pop all the remaining elements and concat with result string
    while not s.is_empty():
        result += s.pop()               
        
    return result



    
# infix to prefix
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


#Machine Problem 2
def infix_to_prefix(infix):
    # reverse the input infix expression
    rev = reverse(infix)
    
    # since the infix exp is reversed, converting it to postfix is applicable
    # we then use the infix_to_postfix method  
    result = infix_to_postfix(rev)
    
    # after converting, reverse again the resulting postfix expression 
    # returned by the infix_to_postfix function
    return reverse(result)


# MAchine Problem 3
def evalPostFix(postfix):
    s = Stack()
    s.new(100)
    
    for ch in postfix:
        # if not operator, push to stack
        if not is_operator(ch):
            s.push(ch)
            
        # if operator, pop two stack elements and apply the operator on these elements
        # then push the result to the stack
        if is_operator(ch):
            second = s.pop()
            first = s.pop()
            
            if ch == '*':
                res = int(first) * int(second)
                s.push(res)
                
            if ch == '/':
                res = int(first) / int(second)
                s.push(res)
            
            if ch == '+':
                res = int(first) + int(second)
                s.push(res)
                
            if ch == '-':
                res = int(first) - int(second)
                s.push(res)
                
            if ch == '^':
                res = int(first)**int(second)
                s.push(res)
                
    # if no more ch, pop and return the remaining element
    # the remaining element is the resulting number of evaluating the postfix expression
    return s.pop()


#Test cases for infix and postfix evaluation
inf= [
    "A+B",
    "A+B/C-D*E",            
    "(A+B)*C+D/(E+F*G)-H",  
    "A-B-C*(D+E/F-G)-H"     
]

postf = [
    "753*51^/+32-+",
    "793/+24*"
]

print("""Select
      1. Infix to Postfix
      2. Evaluate a Postfix Expression
      3. Infix to Prefix
      """)

ch = int(input(">> "))

if ch == 1:    
    infix = input('Please input the infix expression: ')
    print(f'Infix {infix} \n>> Postfix = {infix_to_postfix(infix)}')
    
elif ch == 2:    
    postfix = input('Input the postfix expression to eval: ')
    print(f'Postfix: {postfix} \n>> Answer = {evalPostFix(postfix)}')
    
elif ch == 3:
    infix = input('Please input the infix expression: ')
    print(f'Infix {infix} \n>> Prefix = {infix_to_prefix(infix)}')
    
else:
    print('Invalid selection')

