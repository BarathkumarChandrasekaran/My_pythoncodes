print("\n\nTicket Booking System\n")
restart = ('Y')

while restart != ('N', 'NO', 'n', 'no'):
    print("1.Check PNR status")
    print("2.Ticket Reservation")
    option = int(input("\nEnter your option : "))

    if option == 1:
        print("\nEnter the PNR Number :  ")
        pnr = int(input())
        print(f"Your PNR no {pnr} status is Confirmed, Chart Prepared")
        exit(0)

    elif option == 2:
        people = int(input("\nEnter no. of Ticket you want : "))
        name_l = []
        age_l = []
        sex_l = []
        Phone = []
        for p in range(people):
            name = str(input("\nName : "))
            name_l.append(name)
            age = int(input("\nAge  : "))
            age_l.append(age)
            sex = str(input("\nSex : "))
            sex_l.append(sex)
            phone = int(input("\nContact number :"))
            Phone.append(phone)

        restart = str(input("\nDid you forgot someone? y/n: "))
        if restart in ('y', 'YES', 'yes', 'Yes'):
            restart = ('Y')
        else:
            x = 0
            print("\nTotal Ticket : ", people)
            for p in range(1, people + 1):
                print("Ticket : ", p)
                print("Name : ", name_l [x])
                print("Age  : ", age_l [x])
                print("Sex : ", sex_l [x])
                print("Phone :", Phone[x])
                x += 1




