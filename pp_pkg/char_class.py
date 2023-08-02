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

        if char == '1' or char.lower() == 'warriar':
            char = warr
            while True:
                a = input('Are you use about your chice? Type Yes, Y or No, N: ')
                if a.lower() == 'y' or a.lower() == 'yes' or a.lower() == 'n' or a.lower() == 'no':
                    break
                else:
                    continue

            if a.lower() == 'yes' or a.lower() == 'y':
                input('Then let the adventure begin.')
                break
            elif a.lower() == 'no' or a.lower() == 'n':
                input('Then pick other character.')
                continue
            else:
                input('Invalid input: Returning to Character selecting')

        elif char == '2' or char.lower() == 'theif':
            char = thif
            while True:
                a = input('Are you use about your chice? Type Yes, Y or No, N: ')
                if a.lower() == 'y' or a.lower() == 'yes' or a.lower() == 'n' or a.lower() == 'no':
                    break
                else:
                    continue

            if a.lower() == 'yes' or a.lower() == 'y':
                input('Then let the adventure begin.')
                break
            elif a.lower() == 'no' or a.lower() == 'n':
                input('Then pick other character.')
                continue

        elif char == '3' or char.lower() == 'mage':
            char = mage
            while True:
                a = input('Are you sure you about your chice? Type Yes, Y or No, N: ')
                if a.lower() == 'y' or a.lower() == 'yes' or a.lower() == 'n' or a.lower() == 'no':
                    break
                else:
                    continue

            if a.lower() == 'yes' or a.lower() == 'y':
                input('Then let the adventure begin.')
                break
            elif a.lower() == 'no' or a.lower() == 'n':
                input('Then pick other character.')
                continue

        elif char == '4' or char.lower() == 'archer':
            char = arch
            while True:
                a = input('Are you use about your chice? Type Yes, Y or No, N: ')
                if a.lower() == 'y' or a.lower() == 'yes' or a.lower() == 'n' or a.lower() == 'no':
                    break
                else:
                    continue

            if a.lower() == 'yes' or a.lower() == 'y':
                input('Then let the adventure begin.')
                break
            elif a.lower() == 'no' or a.lower() == 'n':
                input('Then pick other character.')
                continue

        elif char == '5' or char.lower() == 'paladin':
            char = pala
            while True:
                a = input('Are you use about your chice? Type Yes, Y or No, N: ')
                if a.lower() == 'y' or a.lower() == 'yes' or a.lower() == 'n' or a.lower() == 'no':
                    break
                else:
                    continue

            if a.lower() == 'yes' or a.lower() == 'y':
                input('Then let the adventure begin.')
                return char
            elif a.lower() == 'no' or a.lower() == 'n':
                input('Then pick other character.')
                continue

        else:
            input('Invalid Input.  Please type 1-5 or name of the character class.')

