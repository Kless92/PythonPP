warr = "Warrior"
thif = "Theif"
mage = "Mage"
arch = "Archer"
pala = "Paladin"
char = ""

def characterSelection():
    global char
    while True:
        print("Choice from 5 character:\n1.) Warriar\n2.) Theif\n3.) Mage\n4.) Archer\n5.) Paladin")
        char = input(
            "Which woudl you choice?  Type 1-5 or name of the character: ")

        if char == "1" or char.lower() == "warriar":
            char = warr

        elif char == "2" or char.lower() == "theif":
            char = thif

        elif char == "3" or char.lower() == "mage":
            char = mage

        elif char == "4" or char.lower() == "archer":
            char = arch

        elif char == "5" or char.lower() == "paladin":
            char = pala
        else:
            input("Invalid Input.  Please type 1-5 or name of the character class.")
        while True:
            print("Are you use about your chice as a",char,"?") 
            a = input("Type Yes, Y or No, N: ")
            if a.lower() == "y" or a.lower() == "yes" or a.lower() == "n" or a.lower() == "no":
                break
            else:
                continue

        if a.lower() == "yes" or a.lower() == "y":
            input("Then let the adventure begin.")
            return char
        elif a.lower() == "no" or a.lower() == "n":
            input("Then pick other character.")
            continue