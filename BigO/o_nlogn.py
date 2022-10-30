def nLogN(n):
    y=n
    while(n>1):
        n = n/2
        for i in range(1,y+1):
            print(i, end=" ")
        print('')
nLogN(4)