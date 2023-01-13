#Timajo, Kurt Vincent
#CpE-2B
import array as arr
numArr = arr.array('i', []) # main array to be manipulated

#prints the numArr
# parameter:text (for description of the array e.g. updated)
def printArr(text="Array"): 
    """Prints an array of integers

    Args:
        text (str, optional): text description of the printed array. Defaults to "Array".
    """
    print(f'{text}:', end=" ")
    if(len(numArr)==0):
        print('[]')
    else:
        print('[', end="")
        for elem in numArr:
            print(elem, end=" ")
        print(']')        

def removeDuplicate(refArr): 
    """Removes duplicate elements in an array

    Args:
        refArr (array.array): the array whose duplicate elements will be removed

    Returns:
        updated (array.array): the array with no duplicate elements
    """
    noDups = arr.array('i',[]) # 1 4 5 6 7 
    for i in refArr:
        if(i not in noDups):
            noDups.append(i)
        
    return noDups    
    
print('Prob 2: Array Operations')
printArr()
repeat= 'y'
while(repeat == 'y'):
    print("""    Press 1 to append a new item 
    Press 2 to extend new items
    Press 3 to remove duplicate elements
    Press 4 to print last element
    Press 5 to insert an item to a specific index""")
    
    choice = int(input('>> ')) #ask the user to choose a function
    if(choice == 1):
        item = int(input('Enter the item to add: '))
        #append item to numArr
        numArr.append(item)
        printArr()
        
    elif(choice == 2):
        itemsToExt =[]
        items = input('Enter items to add separated by space: ')
        items = items.split()
        #add each item to itemsToExt
        for e in items:
            itemsToExt.append(int(e))
        #extend numArr with itemsToExt
        numArr.extend(itemsToExt)    
        printArr()
        
    elif(choice == 3):
        #pass numArr to removeDuplicate()
        updatedArr = removeDuplicate(numArr)
        #replace each original in numArr with updated (which has no duplicates)
        for i in range(0, len(updatedArr)):
            numArr[i]=updatedArr[i]
            
        #delete each element that are not from updatedArr
        for i in range(len(numArr)-1,len(updatedArr)-1,-1):
            del numArr[i]
        printArr("Updated")
        
    elif(choice == 4):
        print('Last element in Array:', numArr[len(numArr)-1])
        
    elif(choice == 5):
        numToInsert = int(input('Number to insert: '))
        ind=int(input('At index: '))
        numArr.insert(ind,numToInsert)
        printArr("After inserting")
    
    #repeat?yes/no
    repeat = input('Do you want to continue? y/n: ')
    