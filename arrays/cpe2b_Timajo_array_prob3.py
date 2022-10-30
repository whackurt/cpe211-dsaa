#Timajo, Kurt Vincent
#CpE-2B
import array as arr

splitNums = arr.array('i', [])
hasOutOfRange=False

numbers = input('Please input numbers between 30-40 separated by space: ')
numbers = numbers.split() #splitting the input numbers

for num in numbers:
    splitNums.append(int(num))

for eachNum in splitNums:
    if(eachNum < 30 or eachNum > 40): #checks if each value is within 30-40
        #if value is less than 30 or greater than 40, 
        #set hasOutOfRange to True
        hasOutOfRange=True 
        
if(hasOutOfRange): #if out of range
    print('Incorrect range! Please input numbers between 30-40')
else:
    missingNums = arr.array('i', [])
    for i in range(30,41):
        #if i is not in the input numbers, then add to missing
        if(i not in splitNums):  
            missingNums.append(i)

    print('Original array: ', end=" ")
    for e in splitNums:
        print(f'{e}', end=" ")
    print()

    print('Missing array (30-40): ', end=" ")
    for e in missingNums:
        print(f'{e}', end=" ")