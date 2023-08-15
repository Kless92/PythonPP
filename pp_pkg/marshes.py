from pp_pkg import cross_roads, bag, game_over, attacks

marcehsFirst = True
shackFirst = True
oldWomenFirst = True
treeStumpFirst = True
cryptFirst = True
gotKey = False
permission = False
def marshLands(char):
    global marcehsFirst, permission

    if marcehsFirst == True:
        print("The",char,"step inot the 'Marsh Lands'.\nFor only a few noticable land marks, theirs nothing but tall grass going for miles.")
        print("The",char,"notice a small and worn out shack,\na huge Tree Stump,\nand what look like a entrance to a crypt.")
        input("Should check out each one.")
        marcehsFirst = False
    else:
        print("The",char,"reutrned to")
        input("the Marshes Lands")
    
    while True:
        print("1.) Head to the Old Shak\n2.) Head tword the Large Stump.\n3.) Go to the Crypt.\n4.) Leave the area")
        a = input("What should you do: ")

        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue

        if a == "3" or a.lower() == "crypt":
            if oldWomenFirst == True:
                input("There no reason to risk your self there yet.")
                continue
            elif gotKey == True:
                input("You dont need to go there anymore.")
            else:
                theCrypt(char)
                break
        elif a == "1" or a.lower() == "shak" or a.lower() == "old shak" or a.lower() == "oldshak":
            if permission == True:
                input("Dont need to bother her anymore.")
                continue
            else:
                oldShak(char)
                break
        elif a == "2" or a.lower() == "stump" or a.lower() == "large stump" or a.lower() == "largestump":
            largeStump(char)
            break
        elif a == "4" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break

def oldShak(char):
    
    global shackFirst, oldWomenFirst, permission

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
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue

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
                input("She throw a Tourch at you\nand you took it.")
                oldWomenFirst = False
            elif gotKey == True:
                print("The old women poked out of the window and began to chuck")
                print("Your back and I see you kill that Necro Manser whos been keeping me up for the last week.")
                input("Oh sorry, guess I forgot to mention that?.")  
                print("Well now you have the key let me tell you what to do next.\nGo to the Tree Stump and use the key to open the chest.")
                print("Inside is a scroll that will weeken the 'Demon Lord' and maybe you will be able to kill it.")
                print("Oh and what your up against is a 'Demon Lord' so good luck ya.")
                input("She quiet as she closed the window, better head to the Tree Stump.")
                permission = True
                marshLands(char)
            else:
                input("Unless you got what I need im not tell you a thing,\nshe said inside here shack.")
        elif a == "2" or a.lower() == "leave" or a.lower == "exit":
            marshLands(char)
        else:
            bag.invalid

def largeStump(char):

    global treeStumpFirst, permission
    
    if treeStumpFirst == True:
        print("The",char,"approach the Tree Stump.\nIt was bigger up close.")
        print("How a tree grew in the 'Marches' can only be the work of magic")
        print("Then the",char,"noticed a chest underneath it.")
        input("It could have what you need.")
        treeStumpFirst = False
    else:
        print("The",char,"return to the Tree Stump,")
        input("again.")
    while True:
        print("1.) 'Open' the chest.\n2.) 'Leave'")
        a = input("What should you do: ")

        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue

        if a == "1" or a.lower() == "open":
            print("The",char,"tried opening the chest but its locked.")
            while True:
                b = input("If only you had a 'key' or something. ")
                if b.lower() == "key":
                    if bag.useItem(b.lower(), char) == False:
                        continue
                    elif permission == False:
                        oldWomanAtt(char)
                    else:
                        print("The",char,"unlocked the chest.")
                        input("You looked inside.")
                        gotScroll(char)
                elif b.lower() == "lock pick":
                    oldWomanAtt(char)
                else:
                    input("You'll have to try again later.")
                    break
        elif a == "2" or a.lower() == "leave" or a.lower == "exit":
            marshLands(char)
        else:
            bag.invalid

def theCrypt(char):
    print("The",char,"stands at the enters to the crypt.\nYou can feel a frozen breez coming from down below.\nBut like the old women said,")
    input("deep inside is the key. So down you go.")
    print("It feels more cold down here then the breez at the entrence.\nAnd it doesn't help that it pitch black.")

    while True:
        a = input("You'll need your tourch: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a.lower() == "tourch":
            if bag.useItem(a.lower(), char) == False:
                continue
            bag.bag.append("lit tourch")
            input("Your Tourch is now a 'Lit Tourch'.")
            break
        else:
            bag.invalid()
            continue
    
    print("Now the visibility is much better.\nThe",char,"can see row of decaying corpes,\npile on shelves, with some having ther limbs hanging off.")
    input("This crypt is more like a catacomb.")
    print("Suddenly a sound a crakling bones appeared. The",char,"turn and saw a walking skeleton.")
    input("And it was holding a blunt object.")

    while True:
        attacks.attackOptions()
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
                game_over.failedCharge(char, 4)
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                print("The",char,"fired a arrow at the center of the skeleton chest.")
                input("The impact snapped its spine in half.\nIts peice fell to the grown")
                break
            else:
                attacks.noProjectile(char)
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
                attacks.noSpells(char)
                continue
        elif a == "4" or a.lower() == "sneak":
            if char == "Theif":
                print("The",char,"sprint into the shadows and was able to sneak behind the skeleton.")
                input("A quick strack with the daggers hilt and the skeleton fell with a shattered skull.")
                break
            else:
                game_over.sneakFailed(char, 4)
        else:
            bag.invalid()
            continue

    print("Soon more sound of crakling bones and flash scramping off the rough floor fill the Crypt.")
    input("It was invested with undead!")    
    necroFight(char)

def necroFight(char):
    print("Deeper the",char,"venture fighting off more and more of the undead\nuntil a light catchs your eye.\nBlue fire filled a medium size room and bodies were on the floor.")
    print("In the center was a tall clocked man in all back fiddling with a body on a large slab, with tool at his disposal.")
    input("It was a Necro Manser!")
    print("The",char,"held the 'lit tourch' close, back agisnt the wall,")
    input("peaking around the corner staring at the Necro Manser.")

    while True:
        attacks.attackOptions()
        a = input("What should you do: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a == "1" or a.lower() == "charge":
            game_over.necroCharge(char, 5)
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                game_over.necroShoot(char, 5)
            else:
                print("The",char,"doesn't have any projectile weapon.")
                input("So nothing happen.")
                continue
        elif a == "3" or a.lower() == "cast":
            if char == "Mage" or char == "Paladin":
                game_over.necroCast(char, 5)
            else:
                print("The",char,"doesn't know any spells")
                input("So nothing happen.")
                continue
        elif a == "4" or a.lower() == "sneak":
            game_over.necroSneak(char, 5)
        elif a.lower() == "lit tourch":
            if bag.useItem(a.lower(), char) == False:
                continue
            print("The",char,"throw the 'lit tourch' at the Necro Manser")
            print("He then suddenly suddenly vanish as the tourch lands and engult the corps in flames.")
            necroRoundTwo(char)
            break
        elif a.lower() == "elixer of arcan":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                attacks.necroArcan(char)
                necroDeath(char)
        elif a.lower() == "symbol of kings":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                attacks.necroSymbol(char)
                necroDeath(char)
        else:
            bag.invalid()
            continue

def necroRoundTwo(char):
    input("What the hell, he shouted, that was fresh corps; now your dead!")
    while True:
        attacks.attackOptions()
        a = input("What should you do: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a == "1" or a.lower() == "charge":
            if char == "Warrior":
                attacks.necroCharge(char)
                input("Your Great Hammer tore off the Necro Manser as his body fell to the ground.")
                necroDeath(char)
            elif char == "Paladin":
                attacks.necroCharge(char)
                input("Your Great Sword decapitated the Necro Mansers head and his body dropped to the ground.")
                necroDeath(char)
            else:
                game_over.failedCharge(char, 6)
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                print("The",char,"fired a arrow at the Necro Manser, but he suddly disappeared.\nQuickly drawing another arrow, you head the Necro Manser chatting from behind.")
                input("You turn while jumping to your side and fired your arrow.\nIt went thought the Necro Mansers neck as he slowly died chocking on his own blood.")
                necroDeath(char)  
            else:
                attacks.noProjectile(char)
                game_over.necroBlast(char, 6)
        elif a == "3" or a.lower() == "cast":
            if char == "Mage" or char == "Paladin":
                game_over.necroCast(char, 6)
            else:
                attacks.noSpells(char)
                game_over.necroBlast(char, 6)
        elif a == "4" or a.lower() == "sneak":
            if char == "Theif":
                print("The",char,"used a smoke bomb and vanish from the Necro Mansers seights.\nIn the smoke, the",char,"quikcly rush over and stuck the target.")
                input("You took two daggers and table the Necor Mansers back, killing him very quickly.")
                necroDeath(char)
            else:
                game_over.sneakFailed(char, 6)
        elif a.lower() == "elixer of arcan":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                attacks.necroArcan(char)
        elif a.lower() == "symbol of kings":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                attacks.necroSymbol(char)
                necroDeath(char)
        else:
            bag.invalid()
            continue

def necroDeath(char):
    global gotKey
    print("After the fight, the",char,"notic something on the remains of what once was a living person.")
    input("There was a key, must be the same key the Old Women asked you to get.\nBetter take this key and leave this hell hole and quick.")
    bag.bag.append("key")
    input("You found a key.")
    gotKey = True
    marshLands(char)

def oldWomanAtt(char):
    global gotKey

    print("The",char,"successfully unlock the chest.")
    input("Suddenly a chill went down your neck.")
    print("Quick turn around you notic an Old Women with a angry look in her eyes.")
    if gotKey == False:
        print("So you think you can steal from me",char,"?")
        input("Well let me show you what happen to Thieves who crossess a Witch!")
    else:
        print("So you went straight to the chest without even coming to me first?!")
        input("Well looks like I'll have to show you a think or two")
    while True:
        attacks.attackOptions()
        a = input("What should you do: ")

        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue

        if a == "1" or a.lower() == "charge":
            print("The",char,"rush towards the Which but she was too fast")
            game_over.witchCurse(char, 7)
            break
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                print("The",char,"fires at the witch, but she simple deflected it with a spell.")
                game_over.witchCurse(char, 7)
                break
            else:
                attacks.noProjectile(char)
                continue
        elif a == "3" or a.lower() == "cast":
            if char == "Mage":
                print("The",char,"cast a fire ball at the Witch, but she simple deflected it with a spell.")
                game_over.witchCurse(char, 7)
                break            
            elif char == "Paladin":
                print("The",char,"cast Searing Smite at the Witch, but she simple deflected it with a spell.")
                game_over.witchCurse(char, 7)
                break            
            else:
                attacks.noSpells(char)
                continue
        elif a == "4" or a.lower() == "sneak":
            print("The",char,"ran to hid from the Witch, but she keep her eye on locked.")
            game_over.witchCurse(char, 7)
            break
        elif a.lower() == "elixer of arcan":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                print("The power of arcan rush thought your body and you cast arcan explosion on the Witch.")
                input("She never even notice and she suddenly explode.")
                break                
        elif a.lower() == "symbol of kings":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                print("The power of God filled you as you cast a spell this render her immobile.")
                input("Though she still alive, she wont be moving for a while.")
                break
        elif a.lower() == "posion":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                print("The blade was coated wiht posion then you throw it at the wich.\nThough it only hit her should it was enough")
                print("It prevent her from casting any spell which gave you a change to finish her.\nYou Rush here and finished her off.")
                print("Better safe then sorry.")
                break
        else:
            bag.invalid()
            continue
    input("Now you turn your attention to the chest.")
    gotScroll(char)

def gotScroll(char):
    print("Inside the chest was a scroll.\nOn it said its said 'Scroll of Weakening'.\nThis is what the",char,"need to finish the job.")
    input("Time to finish this job!")
    bag.bag.append("scroll of weakening")
    input("You have picked up the Scroll of Weakening")
    cross_roads.doneWithMarshes = True
    cross_roads.theCrossRoads(char)