def power(a,b):
    # base case
    if b==0:
        print('b: ',b)
        return 1;
    
    #recursive statement
    else:
        print('b: ',b)
        return a*power(a,b-1)
    # (b==0) ? (1) : (a*power(a,b-1))
    
    

    
print(power(3,4))
# print(power(2,6))
# print(power(2,0))
# print(power(0,1))
# print(power(1,4))
# print(power(4,3))
# print(power(4,6))
