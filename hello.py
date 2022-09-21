# emp1 = ['John Smith', 35, 'Male', 'CDO']
# emp2 = ['James Bond', 37, 'Male', 'Iligan']
details=['Name', 'Age', 'Gender', 'Address']

# for i in range(0,4):    
#     print(f'{details[i]}: {emp1[i]}')
    
# for i in range(0,4):    
#     print(f'{details[i]}: {emp2[i]}')


emps = [
        ['John Smith', 35, 'Male', 'CDO'], 
        ['James Bond', 37, 'Male', 'Iligan']
]

for i in range(0,len(emps)):
    for j in range(0,len(emps[i])):
        print(f'{details[j]}: {emps[i][j]}')
