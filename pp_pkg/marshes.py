from pp_pkg import cross_roads, bag, game_over

marcehsFirst = True
shackFirst = True
oldWomenFirst = True
treeTrunkFirst = True
cryptFirst = True
def marshLands(char):
    global marcehsFirst

    if marcehsFirst == True:
        print("The",char,"step inot the 'Marsh Lands'.\nFor only a few noticable land marks, theirs nothing but tall grass going for miles.")
        print("The",char,"notice a small and worn out shack,\na huge tree stomp,\nand what look like a entrance to a crypt.")
        input("Should check out each one.")
        marcehsFirst = False
    else:
        print("The",char,"reutrned to")
        input("the Marshes Lands")
    
    while True:
        print("1.) Head to the Old Shak\n2.) Head tword the Large Trunk.\n3.) Go to the Crypt.\n4.) Leave the area")
        a = input("What should you do: ")

        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue

        if a == "3" or a.lower() == "crypt":
            if oldWomenFirst == True:
                input("There no reason to risk your self there yet.")
                continue
            else:
                theCrypt(char)
                break
        elif a == "1" or a.lower() == "shak" or a.lower() == "old shak" or a.lower() == "oldshak":
            oldShak(char)
            break
        elif a == "2" or a.lower() == "trunk" or a.lower() == "large trunk" or a.lower() == "largetrunk":
            largeTrunk(char)
            break
        elif a == "4" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break



def oldShak(char):
    
    global shackFirst 
    global oldWomenFirst

    if shackFirst == True:
        print("The",char,"reach the old shack.\nIt was in worst condition up close,")
        input("but a light can seen though the window.")
        shackFirst = False
    else:
        print("The",char,"return,")
        input("to the shack.")

    while True:
        print("1.) 'Knock' on the 'Door'.\n2.) Leave")
        a = input("What would you do: ")
        if a == "1" or a.lower() == "knock" or a.lower() == "door":
            if oldWomenFirst == True:
                print("After knocking the door, a elderly came out hunched over look at you with one lazy eye open.")
                print("Well well well",char,"what bring you to the 'Marshes'?")
                input("Can't be to just visit a old lady.")
                print("The",char,"explied ot the old women about the job and she only holler.")
                print("You think a",char,"like yourself can kill this beast? Do you even know what your up aginst?")
                input("Well I'm not tell you what it is but I will tell you how to kill it!")
                print("You should notice a crypt not far from here.\nDeep inside is a key, bring it to me and I'll tell you the rest.")
                input("She continue laughing as she return inside and shut the door.\nOh and youll need this!")
                bag.bag.append("tourch")
                input("She throw a Tourch at you.\nThis could help.")
                oldWomenFirst = False
            else:
                input("Unless you got what I need im not tell you a thing,\nshe said inside here shack.")
        elif a == "2" or a.lower() == "leave" or a.lower == "exit":
            marshLands(char)
        else:
            bag.invalid

def largeTrunk(char):

    global treeTrunkFirst
    
    if treeTrunkFirst == True:
        print("The",char,"approach the tree stomp.\nIt was bigger up close.")
        print("How a tree grew in the 'Marches' can only be the work of magic")
        print("Then the",char,"noticed a chest underneath it.")
        input("It could have what you need.")
        treeTrunkFirst = False
    else:
        print("The",char,"return to the tree stomp,")
        input("again.")
    while True:
        print("1.) 'Open' the chest.\n2.) 'Leave'")
        a = input("What should you do: ")

        if a == "1" or a.lower() == "open":
            print("The",char,"tried opening the chest but its locked.")
            while True:
                b = input("If only you had a 'key' or something. ")
                if b.lower() == 'key':
                    if bag.useItem(b.lower(), char) == False:
                        continue
                else:
                    input("You'll have to try again later.")
                    break
        elif a == "2" or a.lower() == "leave" or a.lower == "exit":
            marshLands(char)
        else:
            bag.invalid

def theCrypt(char):
    print("The",char,"stands at the enters to the crypt.\nYou can feel a frozen breez coming from down below.\nBut like the old women said,")
    input("deep inside is the key. So down you go")
    print("It feels more cold then the breez at the entrence.\nAnd it doesn't help that it now pitch black.")

    while True:
        a = input("You'll need the tourch: ")
        if a.lower() == "tourch":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                break
    
    print("Now the visibility is much better.\nThe",char,"can see row of decaying corpes,\npile on shelves, with some having ther limbs hanging off.")
    input("This crypt is more like a catacomb.")
    print("Suddenly a sound a crakling bones appeared. The",char,"turn and saw a walking skeleton.")
    input("And it was holding a blunt object.")

    while True:
        print("1.) Charge\n2.) Shoot\n3.) Cast\n4.) Sneak")
        a = input("What should you do: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a == "1" or a.lower() == "charge":
            if char == "Warrior":
                print("The",char,"charge the skeleton.")
                input("Crushing it with a Great Hammer")
                break
            elif char == "Paladin":
                print("The",char,"charge the skeleton.")
                input("Sliceing it in half with a Great Sword.")
                break
            else:
                game_over.failedCharge(char, 3)
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                print("The",char,"fired a arrow at the center of the skeleton chest.")
                input("The impact snapped its spine in half.\nIts peice fell to the grown")
                break
            else:
                print("The",char,"doesn't have any projectile weapon.")
                input("So nothing happen.")
                continue
        elif a == "3" or a.lower() == "cast":
            if char == "Mage":
                print("The",char,"cast a fire ball at the skeleton.")
                input("Turning it into a pile of ash.")
                break
            elif char == "Paladin":
                print("The",char,"cast Searing Smite at the skeleton.")
                input("Turning it into a pile of ash.")
                break
            else:
                print("The",char,"doesn't know nay spells")
                input("So nothing happen.")
                continue
        elif a == "4" or a.lower() == "sneak":
            if char == "Theif":
                print("The",char,"sprint into the shadows and was able to sneak behind the skeleton.")
                input("A quick strack with the daggers hilt and the skeleton fell with a shattered skull.")
                break
            else:
                game_over.sneakFailed(char, 3)
        else:
            bag.invalid()
    necroFight(char)

def necroFight(char):
    print("Soon more sound of crakling bones and flash scramping off the rough floor fill the Crypt.")
    input("It was invested with undead!")
    print("Deeper the",char,"venture fighting off more and more of the undead\nuntil a light catchs your eye.\nBlue fire filled a medium size room and bodies were on the floor.")
    print("In the center was a tall clocked man in all back fiddling with a body on a large slab, with tool at his disposal.")
    input("It was a Necro Manser!")
    print("The",char,"put down the touch,")
    input("Back aginst the wall, peaking around the corner\nstaring at the Necro Manser.")

    while True:
        print("1.) Charge\n2.) Shoot\n3.) Cast\n4.) Sneak")
        a = input("What should you do: ")