def make_reserve():  # no paramters are needed
    # ask some questions to get people, place, etc.
    # make the reservation data object, probably a list to start with...
    new_reserve = ['Res.#', 'Name', 'Date', 'Time', 'No. of Adults', 'No. of Children', 'No. of Senior Citizen',
                       'Total']
    print()
    new_reserve[0] = reserve_num
    new_reserve[1] = input("Date: ")
    new_reserve[2] = input("Time: ")
    new_reserve[3] = input('Name: ')
    new_reserve[4] = input('No. of Adults: ')
    new_reserve[5] = input('No. of Children: \t')
    new_reserve[6] = input('No. of Senior Citizen: \t')
    new_reserve[7] = int(new_reserve[4]) + int(new_reserve[5]) + int(new_reserve[6])

    print()
    return new_reserve



def view_reserve(reserve):
    # make a loop to loop through the reserve, which is probably
    # a list-of-lists to start with
    for r in reserve:
        print("Res.#   Date \t\tTime \t  Name \t\t# Adults\t# Children \t# Senior Citizen\t Total")
        print(r)
        anykey = input("Press Any Key to Continue")
    # no return is needed for a "print" function, it will return "None" automatically


# make your main loop and have a container to hold the reserve.  This should NOT
# be in a function

# set up the main loop...
reserve_num = 0
list_reserve = []  # to hold all of the reserve...

while True:
    reserve_num = reserve_num + 1
    print()
    print("Welcome to Yan Buffet Restaurant")
    print()
    print("System Menu")
    print("\ta. View all Reservations")
    print("\tb. Make Reservations")
    print("\tc. Delete Reservation")
    print("\td. Generate Report")
    print("\te. Exit")
    print()
    # ask your questions about what to do, call the functions as needed...
    # something like...

    # ask the question, catch the result in a variable called "response"...
    # set up your if-else based on response...
    select = input("Enter Selection: ")

    if select == 'A' or select == 'a':
        view_reserve(list_reserve)

    elif select == 'B' or select == 'b':
        new_res = make_reserve()
        list_reserve.append(new_res)
    elif select == 'C' or select == 'c':
        view_reserve(list_reserve)

    elif select == 'D' or select == 'd':
        print("Rate of the Following: ")
        print("Adult - P500.00 \nChildren - P250.00\n Senior Citizen")

    else:
        break  # stop the loop