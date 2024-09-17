Data = [ ]

def GPA_Checker( ):

    while True:
        First = input("Please enter first name or 'ZZZ' to quit: ")
        if First == ("ZZZ"):
            break
        
        Last = input("Now please enter last name or 'ZZZ' to quit: ")
        if Last == ("ZZZ"):
            break

        GPA = float(input("Enter your GPA (in 0.00 format): "))
        if GPA >= 3.5:
            print(f'Congradulations, {First} {Last} has made the Deans list')
        elif GPA >= 3.24 and GPA < 3.5:
            print(f'Congradulations, {First} {Last} has made the Honor Roll')
        else:
            print(f'Congradulations, {First} {Last} sucks')

        Data.append({"First Name" : First, "Last Name" : Last , "GPA" : GPA})
        for x in Data:
            print(f'{x["First Name"]} {x["Last Name"]} | GPA: {x["GPA"]}')

GPA_Checker()
