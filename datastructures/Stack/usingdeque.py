from collections import deque

url = 'https://ustp.edu.ph'

stack = deque()
print(stack)


stack.append(f'{url}/cdo') #top: cdo
print(stack)
# # print('Top:'stack[0])

stack.append(f'{url}/claveria') #top: claveria
print(stack)
print('Top:',stack[-1])

stack.append(f'{url}/panaon') #top: panaon
print(stack)
print('Top:',stack[-1])


# stack.append(f'{url}/villanueva') #top: villanueva
# print(stack)
# print('Top:',stack[-1])

stack.pop() #top: panaon
print(stack)

stack.pop() #top: claveria
print(stack)

# stack.pop() #top: cdo
# print(stack)

# stack.pop() #top: none
# print(stack)