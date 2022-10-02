
#list of all reservations
reservations = [
    #[res_no, name, res_date, res_time, adults, children, SC]
]

def view_all_reservations():
    print('\n\t\t======================================= All Reservations ======================================')
    print('\t\tRes #\tName\t\tDate\t\tTime\t\t# of Adults\t# of Children\t# of SC')
    if(len(reservations) == 0):
        print('\t\t\t\t\t\t\tNo Reservations yet')
    for res in reservations:
        #display each reservation in list
        print(f'\t\t{res[0]}\t{res[1]}\t{res[2]}\t{res[3]}\t{res[4]}\t\t{res[5]}\t\t{res[6]}')
    
    print('\t\t===============================================================================================')
        
    print('\n')    
    menu()


def make_reservation():    
    #list for new single reservation
    reservation = []
    
    print('\t============= Make a Reservation =============\n')
    name = input('\t\tName (First Last): ')
    res_date = input('\t\tDate (mm/dd/yyyy): ')
    res_time = input('\t\tTime (hh:mm am/pm): ')
    no_adults = int(input('\t\tNo. of Adults: '))
    no_children = int(input('\t\tNo. of Children: '))
    no_sencitizen = int(input('\t\tNo. of Senior Citizen: '))
    
    #generate reservation number
    res_num = int((len(reservations)+1))
    for res in reservations:
        #check if generated res_num is equal to any existing reservation number
        if(res[0] == res_num):
            #if equal, add 1 to the generated number
            res_num = res_num + 1 
            
    
    #add items to reservation
    reservation.append(res_num) 
    reservation.append(name)
    reservation.append(res_date)
    reservation.append(res_time)
    reservation.append(no_adults)
    reservation.append(no_children)
    reservation.append(no_sencitizen)
    
    #appending the new reservation to the main reservations list
    reservations.append(reservation)
        
    print("Reservation successfully added")
    
    view_all_reservations()    
    menu()
       
    
def delete_reservation(res_no):
    found = 0
    for res in reservations:
        if(res[0] == res_no):
            found=1
            reservations.remove(res)
            print(f'\tReservation number {res_no} is now deleted.\n')
            
    #to handle non-existing reservation number
    if(not found):
        print(f'Reservation with number {res_no} is not found.')
    
    view_all_reservations()
    menu()
    
def calculate_total(res):
    print('\n\n**************** Reservation Report ****************')
    print('\tReservation #', res[0])
    print(f'\n\tTotal Number of Adults: {res[4]}')
    print(f'\tTotal Number of Children: {res[5]}')
    print(f'\tTotal Number of Senior Citizen: {res[6]}\n')
    
    #res[4] no. of adults
    #res[5] no. of children
    #res[6] no. of SC's 
    total_guests = res[4] + res[5] + res[6]
    
    adults_total = 500*res[4]
    children_total = 250*res[5]
    sencitizen_total = 400*res[6]
    
    grand_total = adults_total + children_total + sencitizen_total
    
    print(f'\tTotal Guests: {total_guests}')
    print(f'\tGrand Total: P{float(grand_total)}')    
    print('***************************************************')
    
def generate_report(res_no):
    found = 0
    for res in reservations:
        if(res[0] == res_no):
            found=1
            #pass the list to calculate_total
            calculate_total(res)

    #handle non-existing reservation number
    if(not found):
        print(f'Reservation with number {res_no} is not found.')
    
    menu()

print('Welcome to Yan Buffet Restaurant')

def menu():    
    print('\nSystem Menu')
    print('\ta. View all Reservations\n\tb. Make Reservations\n\tc. Delete Reservations\n\td. Generate Report\n\te. Exit')
    opt = input('>> ')
    if(opt == 'a' or opt == 'A'):
        view_all_reservations()
        
    elif(opt == 'b' or opt == 'B'):
        make_reservation()
        
    elif(opt == 'c' or opt == 'C'):
        print('============= Delete a Reservation =============\n')
        res_no = int(input('Reservation no. : '))
        delete_reservation(res_no)
        
    elif(opt == 'd' or opt == 'D'):
        print('============= Generate a Report =============\n')
        res_no = int(input('Reservation no. : '))
        generate_report(res_no)
        
    elif(opt == 'e' or opt == 'E'):
        print('\n\nYan Buffet Restaurant is happy to serve you. Thank you!\nDeveloped by Kurt Timajo')
        exit()
    
    else:
        print('\n!!! Invalid Input !!!')
        menu()
               
        
menu()