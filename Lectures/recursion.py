def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
    
print(fact(7))
print(fact(8))
print(fact(9))

def manual_multiply(n1,n2):
    if(n2==0):
        return 0
    else:
        return n1+(manual_multiply(n1, n2-1))

print(manual_multiply(2,3))
print(manual_multiply(4,3))
print(manual_multiply(6,12))
