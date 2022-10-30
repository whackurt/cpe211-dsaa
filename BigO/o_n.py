given_array=[1,2,3,4,5]
larger_array=[2,4,6,8,10,1,3,5,7]

def findSum(arr):
    total=0
    for i in arr:
        total+=i
    return total

print(findSum(larger_array))
    
    
    