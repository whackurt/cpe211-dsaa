for question in range(2):
    score = 0
    attempts=2


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
        break

    if (score ==2):
        print("you've pass the test")
    ask = input("do you want to try again? (yes or no):")
    if (ask=="yes"):
        attempts -=1
        print("Remaining attempts:", attempts)
        print("Answer the following question below:")
    if (ask=="no"):
        exit()

    if (score==1):
        print("your score is low")
        
    ask2 = input("do you want to try again? (yes or no):")
    if (ask2=="yes"):
        attempts -= 1
        print("Remaining attempts:", attempts)
        print("Answer the following question below:")
        if (ask2=="no"):
            exit()

    if (score==0):
        print("no score")
    ask3 = input("do you want to try again? (yes or no):")
    print(ask3)
    if (ask3 == "yes"):
        attempts -= 1
        print("Remaining attempts:", attempts)
        print("Answer the following question below:")
    if (ask3=="no"):
        exit()