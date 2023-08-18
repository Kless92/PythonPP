from pp_pkg import bag

""" warr = "Warrior"
thif = "Theif"
mage = "Mage"
arch = "Archer"
pala = "Paladin"
char = "" """

class myCharClass:
    def __init__(self, name, weapon, spell):
        self.name = name
        self.weapon = weapon
        self.spell = spell

def characterSelection():
    global char
    
    while True:
        print("Type h or help for tips.")
        print("Choice a class from 5 characters:\n1.) Warriar\n2.) Theif\n3.) Mage\n4.) Archer\n5.) Paladin")
        char = input("Which class would you choice?  Type 1-5 or name of the character: ")
        
        if bag.helpMe(char) == True:
            continue
        if char == "1" or char.lower() == "warriar":
            char = myCharClass("Warrior", "Great Hammer", "")
            print("Large Muscular fighter, carrys a",char.weapon,"and prevers a Full Frontal Assult.")
            #char = warr
        elif char == "2" or char.lower() == "theif":
            char = myCharClass("Theif", "Daggers", "")
            print("Skinny but lengthy, uses",char.weapon,", Posions and fights in the Shadows")
            #char = thif
        elif char == "3" or char.lower() == "mage":
            char = myCharClass("Mage", "", "Fire Ball")
            print("Tall and skinny, master of the Arcane, favorit spell is",char.spell,"has no need for Weapons and fight with Spells.")
            #char = mage
        elif char == "4" or char.lower() == "archer":
            char = myCharClass("Archer", "Bow", "")
            print("Not too tall but not too thin, uses a",char.weapon,"for distant combat relying on Precision and Accuracy.")
            #char = arch
        elif char == "5" or char.lower() == "paladin":
            char = myCharClass("Paladin", "Great Sword", "Searing Smite")
            print("Large but not completly strong, using",char.spell,"and a",char.weapon,"and Lawfuly Good")
            #char = pala
        else:
            input("Invalid Input.  Please type 1-5 or name of the character class.")
            continue

        while True:
            print("Are you use about your chice as a",char.name,"?") 
            a = input("Type Yes, Y or No, N: ")
            if a.lower() == "y" or a.lower() == "yes" or a.lower() == "n" or a.lower() == "no":
                break
            else:
                continue

        if a.lower() == "yes" or a.lower() == "y":
            input("Then let the adventure begin.")
            return char
            break
        elif a.lower() == "no" or a.lower() == "n":
            input("Then pick other character.")
            continue