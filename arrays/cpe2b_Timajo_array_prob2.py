#Timajo, Kurt Vincent
#CpE-2B
import array as arr
numArr = arr.array('i', [])

def printArr(text="Array"):
    print(f'{text}:', end=" ")
    if(len(numArr)==0):
        print('[]')
    else:
        print('[', end="")
        for elem in numArr:
            print(elem, end=" ")
        print(']')        
    
def removeDuplicate(refArr):
    updated = arr.array('i',[])
    for i in refArr:
        if(i not in updated):
            updated.append(i)
    return updated    
    
print('Prob 2: Array Operations')
printArr()
repeat= 'y'
while(repeat == 'y'):
    print("""    Press 1 to append a new item 
    Press 2 to extend new items
    Press 3 to remove duplicate elements
    Press 4 to print last element
    Press 5 to insert an item to a specific index""")
    
    choice = int(input('>> '))
    if(choice == 1):
        item = int(input('Enter the item to add: '))
        numArr.append(item)
        printArr()
        
    elif(choice == 2):
        itemsToExt =[]
        items = input('Enter items to add separated by space: ')
        items= items.split()
        for e in items:
            itemsToExt.append(int(e))
        numArr.extend(itemsToExt)    
        printArr()
        
    elif(choice == 3):
        updatedArr = removeDuplicate(numArr)
        for i in range(0, len(updatedArr)):
            numArr[i]=updatedArr[i]
        
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
    
    repeat = input('Do you want to continue? y/n: ')
    