from pp_pkg import cross_roads, bag, attacks, game_over

mountFirst = True


def mountains(char):
    global mountFirst

    if mountFirst == True:
        print("The", char, "reach the base of the mountions.")
        input("You see wide stair case and looking up to see it leads to a large cave entrance.")
        mountFirst = False
    else:
        print("The", char, "reutrned to")
        input("the Mountains")

    while True:
        print("1.) Go up stair case\n2.) Head towards the Low Cave.\n3.) Take the Odd Path\n4.) 'Leave' the area")
        a = input("What should you do: ")

        if a == "1" or a.lower() == "go" or a.lower() == "enter":
            print("The", char, "sense something dangerous moving forword.")
            a = input("Are you sure you want to continue: ")
            if a.lower() == "y" or a.lower() == "yes":
                highPoint(char)
            elif a.lower() == 'n' or a.lower() == "no":
                continue
            else:
                bag.invalid()
        elif a == "2" or a.lower() == "cave" or a.lower() == "low cave" or a.lower() == "lowcave":
            lowCave(char)
        elif a == "3" or a.lower() == "left" or a.lower() == "path" or a.lower() == "odd path" or a.lower() == "oddpath":
            oddPath(char)
        elif a == "4" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break


def highPoint(char):
    print("The", char, "scale the long stair case till the entrance was reached.")
    input("Inside the monster that was terrorize the town was there.")
    print("It was floating in the air,\nwith its legs cross, completly still\nlike it was meditating.")
    print("Its feet replace with hoves, its skin is the color of blood, 2 large horns were on it head and look about 20 feet tall.")
    input("You came face to face with a 'Demon Lord'!\nLucky you didn't notice you so the element of surprise is on your side.")
    demonLordIncounter(char)


def lowCave(char):
    print(char)


def oddPath(char):
    print(char)


def demonLordIncounter(char):
    while True:
        attacks.attackOptions()
        a = input("What should you do: ")

        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue

        if a == "1" or a.lower() == "charge":
            print("The", char, "charges towards the 'Demon Lord',")
            input("but in that moment, its eye opend before you could touch him")
            game_over.firstSrikeDemon(char, 8)
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                print("The", char, "fires a arrow at the 'Demon Lord',")
                input("but it only ricochet off it.\nThen its eyes open.")
                game_over.firstSrikeDemon(char, 8)
            else:
                attacks.noProjectile(char)
                continue
        elif a == "3" or a.lower() == "cast":
            if char == "Mage" or char == "Paladin":
                print("The", char, "prepares to cast a spell on the 'Demon Lord',")
                input("but its eyes open before the spell could be cast.")
                game_over.firstSrikeDemon(char, 8)
            else:
                attacks.noSpells(char)
                continue
        elif a == "4" or a.lower() == "sneak":
            print("The", char, "try to sneak up to the 'Demon Lord' but its")
            input("sense was more powerful the most foes and ite eye open.")
            game_over.firstSrikeDemon(char, 8)
        elif a.lower() == "scroll of weakening":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                input("The 'Scroll of Weakening' turn to dust after use.")
                demonLordFight(char)
        else:
            bag.invalid()


def demonLordFight(char):
    pass
