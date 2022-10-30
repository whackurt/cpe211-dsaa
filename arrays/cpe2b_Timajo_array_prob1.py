#Timajo, Kurt Vincent
#CpE-2B
import array as arr 

def printArr(text,arr,rev=False):
    print(text, end=" ")
    if(not rev):
        for e in arr:
            print(e, end=" ")
    elif(rev==True):
        for i in range(len(arr)-1,-1,-1):
            print(arr[i], end=" ")
    

nums = arr.array('i',[])
print('Input 10 numbers separated by space')
inputNums = input()
splitNums = inputNums.split()
spLen = len(splitNums)

if(spLen<10): #handling less than 10 elements
    print(f'Lacking {10 - spLen} element/s')
elif(spLen>10): #handling more than 10 elements
    print(f'You have entered more than 10 elements')
else: #handling exact 10 elements
    for eachNum in splitNums:
        nums.append(int(eachNum))
    
    printArr('Original:', nums)
    print()
    printArr('Reverse:', nums, rev=True)
    print()
    printArr('Ascending:', sorted(nums))
    print()
    printArr('Descending:', sorted(nums, reverse=True))


        
