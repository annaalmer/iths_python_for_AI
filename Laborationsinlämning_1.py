#-------------------------------------------------------------------------
# Projekt 3: Sten, sax eller påse
#-------------------------------------------------------------------------
import random

set = ("sten", "sax", "påse")

while True:

    computersChoice = set[random.randint(0,2)]  

    print("Sten, sax eller påse?")
    print("1. Sten")
    print("2. Sax")
    print("3. Påse")

    usersChoiceString = input("Ange ditt val, 1-3: ")
    usersChoiceInt = int(usersChoiceString) if usersChoiceString.isdecimal() else None

    if(usersChoiceInt not in range(1,4)):
        print("Ogiltigt val. Prova igen.")
        continue

    usersChoice = set[usersChoiceInt-1]

    print(f'Datorn har {computersChoice}. \nDu har {usersChoice}.')

    if(computersChoice == usersChoice):
        print("Oavgjort! Ny omgång!")
    elif(computersChoice == set[0] and usersChoice == set[1]):
        print("Datorn vann!")
        break
    elif(computersChoice == set[0] and usersChoice == set[2]):
        print("Du vann!")
        break
    elif(computersChoice == set[1] and usersChoice == set[0]):
        print("Du vann!")
        break
    elif(computersChoice == set[1] and usersChoice == set[2]):
        print("Datorn vann!")
        break
    elif(computersChoice == set[2] and usersChoice == set[0]):
        print("Datorn vann!")
        break
    elif(computersChoice == set[2] and usersChoice == set[1]):
        print("Du vann!")
        break
#-------------------------------------------------------------------------