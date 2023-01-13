# importing "array" for array creations
import array as arr

#Append/Extend element
#initialize
myArray = arr.array('i', [1,2])
# myDouble = arr.array('d', [1.5,2.7])
print(myArray)
# for e in myArray:
#     print(e)

                # (0,2)
# for e in range(0,len(myArray)):
#     print(myArray[e])
    
myArray.append(3)
print(myArray)

# for e in myArray:
#     print(e)

myArray.extend([-4,5]) 
print(myArray) #output in line 23

#Read/Print 
# for e in myArray: 
#     print(e, end=" ")
# for e in range(0,len(myArray)):
    # print(myArray[e], end=" ")

#[1,2,3,-4,5,]
#Update/Modify element
myArray[1] = -2
myArray[0] = -1
print(myArray)

#Delete element
myArray.remove(myArray[2])
myArray.remove(-4)
print(myArray)

myArray.extend([6,6])
print(myArray)
# myArray.remove(6)

for x in range(len(myArray)-1,-1,-1):
    if myArray[x] == 6:
        del myArray[x]

print(myArray)
