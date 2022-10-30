from array import *
import math


def printArray(arr):    
    print('Printing array')
    for x in arr:
        print(x)
        


array1 = array('i', [10,20,30,40,50])
printArray(array1)

# accessing
print(array1[0])
print(array1[1])

array1.insert(int(len(array1)/2), 60)
printArray(array1)

#deletion
array1.remove(50)
print('after removing 50')
printArray(array1)

#search
num = 40
i = array1.index(num)
print(f'element with index {i}: {array1[i]}')

#update
array1[i] = 80
print(f'after replacing {num} with 80')
printArray(array1)



a = array('i', [2,4,6,8])
#length 
print(len(a))

#adding
a.append(10)
printArray(a)

a.extend([13,15])
printArray(a)

a.insert(int(len(a)/2), 16)
printArray(a)

import array as arr
#removing
numbers = arr.array('d',[10.5,12.6,14.4,13.8])
numbers2 = arr.array('d',[10.5,12.6,14.4,13.8])
printArray(numbers)
numbers.remove(12.6)
printArray(numbers)
print('removed ',numbers.pop(0))

#concat
s = numbers+numbers2
print('concat=',s)
printArray(s)

#slicing
print(s[2:5])
print(s[:5]) #start to end
print(s[5:]) #6th to end
print(s[:]) #all

#sorting
print(sorted(s))
print(sorted(s, reverse=True))




import numpy as np

c= np.array([12,24,36,48,60])
print(c)

#2D and 3x3
twoD = [
    [1,3,5],
    [2,4,6],
    [3,6,9]
]

print(twoD)
print(twoD[1][1])
twoD[1][1] = 7
print('replaced 4 with 7',twoD)

#3D arr
threeD = np.array([
    [[2,4],[6,8],[10,12]],
    [[3,6],[9,12],[15,18]],
    [[5,10],[15,20],[25,30]]    
])
print(threeD)
print(threeD[2][2][0]) #printing 25