from pp_pkg import bag

warr = "Warrior"
thif = "Theif"
mage = "Mage"
arch = "Archer"
pala = "Paladin"
char = ""

def characterSelection():
    global char
    while True:
        print("Type h or help for tips.")
        print("Choice a class from 5 characters:\n1.) Warriar\n2.) Theif\n3.) Mage\n4.) Archer\n5.) Paladin")
        char = input("Which class would you choice?  Type 1-5 or name of the character: ")
        
        if bag.helpMe(char) == True:
            continue
        if char == "1" or char.lower() == "warriar":
            print("Large Muscular fighter, carrys a Great Hammer and prevers a Full Frontal Assult.")
            char = warr
        elif char == "2" or char.lower() == "theif":
            print("Skinny but lengthy, uses Daggers, Posions and fights in the Shadows")
            char = thif
        elif char == "3" or char.lower() == "mage":
            print("Tall and skinny, master of the Arcane, has no need for Weapons and fight with Spells.")
            char = mage
        elif char == "4" or char.lower() == "archer":
            print("Not too tall and not too fine, a Distance fighter with Precision and Accuracy.")
            char = arch
        elif char == "5" or char.lower() == "paladin":
            print("Large but not completly strong, using Holy Magic and Great Sword and Lawfuly Good")
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