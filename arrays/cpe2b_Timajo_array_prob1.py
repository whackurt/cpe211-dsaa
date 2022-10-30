#Timajo, Kurt Vincent
#CpE-2B
import array as arr 


def printArr(text,arr,rev=False):
    """Prints an array of integers

    Args:
        text (str): describes the printed array e.g. Original, Reverse, Ascending/Descending
        arr (array.array): array whose values will be printed
        rev (bool, optional): tells function to print the array items in reverse order. Defaults to False.
    """
    print(text, end=" ")
    if(not rev): #default order of the array elements
        for e in arr:
            print(e, end=" ")
    elif(rev==True): #reverses the order of elements in the array
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
    
    printArr('\nOriginal:', nums)
    printArr('\nReverse:', nums, rev=True)
    printArr('\nAscending:', sorted(nums))
    printArr('\nDescending:', sorted(nums), rev=True)


        
