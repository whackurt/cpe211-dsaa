#type conversion
print(float(5))
print(int(3.5))
print(str(24))

my_string = 'Hello world'
nums = [1,2,3,4]
list_to_set = set(nums)
set_to_tuple = tuple(list_to_set)
print(list_to_set)
print(set_to_tuple)
print(list(my_string))

#implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print('datatype of num_int: ', type(num_int))
print('datatype of num_flo: ', type(num_flo))
print('value of num_new: ', num_new)
print('datatype of num_new: ', type(num_new))

num_str = '456'
print('datatype of num_str: ', type(num_str))
print(num_int+num_str)

#explicit type conversion
num_str = int(num_str)
print(num_int+num_str)


#print, i/o, import
print(1,2,3,4,)
print(1,2,3,4,sep='*') #with separator
print(1,2,3,4,sep='#', end='&') #with separator and end format

#str.format
num_burgers = 3
drink = 'coke'
print('I want {} burgers and {} as drink'.format(num_burgers,drink))
print('I want {num_burgers} burgers and {drink} as drink'.format(num_burgers=6,drink='sprite'))

# using % operator similar in C
x = 12.34567
print('The value of x is %3.3f' %x)

#input 
num = input('Enter a number: ')
print(f'num={int(num)}')
print(eval('3+8'))


#importing
import math 
print('pi={}'.format(math.pi))

import sys
print(sys.path)
print(sys.path[0])

#arithmetic operators 

x=17
y=8
print(x+y, x-y, x/y, x*y)
print(x**2)
print(x>y, x<y, x==y, x!=y, x>=y, x<=y) #True False False True True False

x=True
y=False
if(x and y):
    print(x and y)
if(x or y):
    print(x or y)
print('Not x is ', not x)


#Bitwise operators
a=9
b=16
print(a&b, a|b, ~a, a^b, a>>2, a<<2)

#identity operator

x1 = 5
y1 = 5
x2 = 'Hey'
y2 = 'Hey'
x3 = [2,4,6]
y3 = [2,4,6]

print(x1 is y1, x2 is not y2, x3 is y3)

#membership operator
x5 = 'Hello world'
y5 = {1:x3,2:y2}

print('e' in x5)
print('Hey' in y5[2])
print(1 in y5)
print('a' in y5[1])

#if-else
num = -9
if num >= 0:
    if(num==0):
        print('Num is zero')
    else:
        print('Positive')
else:
    print('Negative')


#loops 
#range(start, end, steps)
print(range(0,100))
print(list(range(0,100,4)))
print(len(list(range(0,100,4))))

digits = [0,1,5]

# for loop with else
for i in digits:
    print(i)
else:
    print('No items left')

student_name = 'Kurt'
marks = {
    'Kurt': 90,
    'Jules': 55,
    'Arthur': 77
}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry found with that name.')

# while loop with else
counter = 0 
while counter < 5:
    print('Inside City')
    counter+=1
else:
    print('Outside City')
    
#activity on loops
start=25
end=50

for num in range(start, end+1):
    if num > 1:        
        for j in range(2,num):
            if (num % j) == 0:         
                break
        else:
            print(num)

#break and continue
my_str = 'String'
print('\Break')
for char in my_str:
    if char == 'n':
        break 
    print(char)

print('\nContinue')
for char in my_str:
    if char == 'i':
        continue 
    print(char)

#pass 
def myfunc(num):
    pass

print(myfunc(7))

#functions 

#function with default argument
def greet(name, msg="have a good day!"):
    """_summary_

    Args:
        name (_type_): _description_
        msg (str, optional): _description_. Defaults to "have a good day!".
    """
    print(f'Hello {name}, {msg}')

print(greet.__doc__)
greet('Kate')
greet('Kate', 'I love you <3')

#func with keyword argument
def greet_friend(name, msg):
    """_summary_

    Args:
        name (_type_): _description_
        msg (_type_): _description_
    """
    print(f'Hello {name}, {msg}')
    
greet_friend(name='Kurt', msg='amping')


#func with arbitrary argument
def greet_many(*friends):
    """_summary_
    """
    for friend in friends:
        print(f'Musta na ka, {friend}')
        
greet_many('Angelo', 'Nino', 'Kent')