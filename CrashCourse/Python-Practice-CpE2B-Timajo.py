#Hello world
# print('Hello world')

#comments Ctrl + /
# print('Hello world') 
# print('Hello world')

#Literal collections
fruits = ["apple", "mango", "orange",["banana", "papaya"]] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i', 'o', 'u', 'u'} #set, (must not have duplicate items, only one 'u' is printed')

print(fruits[3][1])
print(numbers[2])
print(alphabets['c'])
print(vowels) 

#checking type with isinstance function
checkType = isinstance(vowels,set)
print(checkType)

#Employee Data using list
emp1 = ['John Smith', 35, 'Male', 'CDO']
emp2 = ['James Bond', 37, 'Male', 'Iligan']
details=['Name', 'Age', 'Gender', 'Address']

for i in range(0,4):    
    print(f'{details[i]}: {emp1[i]}')
print('\n')
for i in range(0,4):    
    print(f'{details[i]}: {emp2[i]}')

#alternative way (using 2D array)
emps = [
    ['John Smith', 35, 'Male', 'CDO'], 
    ['James Bond', 37, 'Male', 'Iligan']
]
for i in range(0,len(emps)):
    for j in range(0,len(emps[i])):
        print(f'{details[j]}: {emps[i][j]}')


#tuples (immutable)
t = (15.5, 'programming', 20, 'windows 10')

print(t[1:3])
print(t[2:4])

#Strings
s = 'Hello World'

print(s[0], s[2], s[6])

#reversing the string
for i in reversed(range(0,len(s))):
    print(s[i], end=' ')

#alt way to reverse
i= len(s)-1
while(i>=0):
    print(s[i], end='')
    i-=1
print('')

#list
a = [5, 10, 15, 20, 25, 30, 35, 40]
print(a[2])
print(a[0:3])
print(a[5:])
a[6] = 55
print(a[5:])

#sets 
# #sets are unindexed therefore items cannot be accessed by index
myset = {1,2,3,'kurt'}
print(myset)
    
#Dictionary 
my_car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(my_car['brand'])
print(my_car['model'])

#Input/Output
name = input('Name: ')
english_grade = input('English Grade: ')
science_grade = input('Science Grade: ')
math_grade = input('Math Grade: ')

print(f'\nName: {name}') 
print(f'English Grade: {english_grade}')
print(f'Science Grade: {science_grade}')
print(f'Math Grade: {math_grade}')



