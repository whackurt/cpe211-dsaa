student_marks = {}

n = int(input())

for i in range(n):
    marks = []
    name_marks = input()
    marksSplit = name_marks.split()
    for j in range(1,4):
        marks.append(float(marksSplit[j]))        
    student_marks[marksSplit[0]] = marks

query_name = input()
total_marks = 0

for mark in student_marks[query_name]:
    total_marks+=mark

ave = total_marks/3

print('{:.2f}'.format(ave))
    