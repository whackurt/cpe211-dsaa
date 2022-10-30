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
    





















