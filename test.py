attempts=2
ask ='yes'
while(ask == 'yes' and attempts > 0):
    score = 0
    
    print('\nAnswer the questions')
    print("how many days in a year?")
    print("a. 365 b.360 c.370 d.375")
    answer1 = (input("Enter Answer: "))
    if (answer1 == "a") or (answer1 == "A"):
        score += 1

    print("how many days in a week?")
    print("a. 9 b.5 c.7 d.8")
    answer2 = (input("Enter Answer: "))
    if (answer2 == "c") or (answer2 == "C"):
        score += 1

    print("how many color og the rainbow?")
    print("a. 5 b.7 c.8 d.10")
    answer3 = (input("Enter Answer: "))
    if (answer3 == "b") or (answer3 == "B"):
        score +=1

    print("Total_score:", score)
    if (score == 3):
        print("Good job Perfect Score")

    if (score ==2):
        print("you've pass the test")
            
    if (score==1):
        print("your score is low")
    
    attempts-=1    
    
    if(attempts > 0):
        print('Attempt remaining:', attempts)
    else:
        print('End of the quiz. No more attempts left')
        break
        
    ask = input("do you want to try again? (yes or no):")
    if(ask == 'no'):
        print('Thanks for taking the quiz.')
        break
    