classA =[]
for _ in range(int(input('No. of students: '))):
    single = []
    name = input('Name: ')
    score = input('Score: ')
        
    single.append(name)
    single.append(float(score))
    classA.append(single)

scores = []
count=0
for stude in classA:    
    if stude[1] not in scores:
        scores.append(stude[1])    

sorted_scores = sorted(scores, reverse=True)
    
stude_2ndlowest=[]
for student in classA:
    if(student[1] == sorted_scores[len(sorted_scores)-2]):
        stude_2ndlowest.append(student[0])

for name in sorted(stude_2ndlowest):
    print(name)