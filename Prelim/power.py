def power(a,b): 
    # base case
    if b==0:
        print('b: ',b)
        return 1
    
    #recursive statement
    else:
        print('b: ',b)
        return a*power(a,b-1)
    
print('result: ',power(2,4)) # 16





















