#recursive function
def sum_numbers(n):
    #base case: n=0
    if(n==0):
        return 0
    else:
        #traverses nums items
        return nums[n-1]+sum_numbers(n-1)
    

#input to specify the length of list
n = int(input('Count of numbers to input: '))

#initialize an empty list
nums = []

#input number for n times
for x in range(0,n):
    num = int(input(f'Number{x+1}: '))
    #add each input num to nums list
    nums.append(num)

#pass n to sum_numbers summing up of list items
print('\nSum using recursion: {}'.format(sum_numbers(n)))

sumNums = 0
for element in nums:
    sumNums += element

print('sumNums = ',sumNums)

    




