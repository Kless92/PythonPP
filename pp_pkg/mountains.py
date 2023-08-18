from pp_pkg import cross_roads, bag, attacks, game_over

mountFirst = True
improvedWepon = False
caveFirst = False

def mountains(char):
    global mountFirst, caveFirst, improvedWepon

    if mountFirst == True:
        print("The", char.name, "reach the base of the mountions.")
        print("You see wide stair case and looking up to see it leads to a large cave entrance.")
        input("But you also notice a 'Cave Entrance' to the left.")
        mountFirst = False
    else:
        print("The", char.name, "reutrned to")
        input("the Mountains")

    while True:
        print("1.) Go up stair case\n2.) Head towards the 'Cave Entrance'.\n3.) 'Leave' the area")
        a = input("What should you do: ")

        if a == "1" or a.lower() == "go" or a.lower() == "enter":
            print("The", char.name, "sense something dangerous moving forword.")
            a = input("Are you sure you want to continue: ")
            if a.lower() == "y" or a.lower() == "yes":
                highPoint(char)
            elif a.lower() == 'n' or a.lower() == "no":
                continue
            else:
                bag.invalid()
        elif a == "2" or a.lower() == "cave" or a.lower() == "low cave" or a.lower() == "lowcave":
            if 'scroll of weakening' not in bag.bag and caveFirst == False:
                caveFirst = lowCave(char)
            elif "scroll of weakening" in bag.bag and caveFirst == True and improvedWepon == False:
                improvedWepon = lowCaveReturn(char)
            elif "scroll of weakening" not in bag.bag and caveFirst == True:
                input("There no reason to go back there yet.")
                continue
            elif improvedWepon == True:
                input("Theres no reason to go there anymore.")
                continue
            elif 'scroll of weakening' in bag.bag and improvedWepon == False :
                improvedWepon = lowCave2(char)

        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break
        elif bag.threeActions(a) == True:
            continue
        else:
            bag.invalid()

def lowCave(char):
    print("The",char.name,"came to 'Cave Entrance'\nand inside you notice a 'Old Man', praying to a statue.")
    input("I knew you would come, said the 'Old Man'")
    print("On the top of the mountain is a threat to the people of this land, but you already knew that.")
    print("But no weapon or magic will be to kill it.\nYou'll need a power hidden in the 'Marsh Land'")
    input("fine the 'Old Women' there she will you what to do.")
    input("You dont understand what he was talking about\nbut it may be a clue to what you need.")
    return True

def lowCave2(char):
    print("The",char.name,"came to 'Cave Entrance'\nand inside you notice a 'Old Man', praying to a statue.")
    input("I knew you would come, said the 'Old Man'")
    print("On the top of the mountain is the threat to the people of this land, but you already knew that.")
    print("But no weapon or magic will be able to kill it.\nBut I sense the scroll from 'Marsh Land' is on you.")
    oldMansEnhance(char)
    return True

def lowCaveReturn(char):
    print("The",char.name,"return to the 'Cave Entrance' with the scroll.")
    input("You returned, said the 'Old Man', and you have the scroll; Good.")
    oldMansEnhance(char)
    return True


def oldMansEnhance(char):
    input("This scroll will weaken this threat but you will need a stronger weapon to destory it.\nOr someone thing that would enchance magic.")
    if char.name == "Warrior" or char.name == "Theif" or char.name == "Archer" or char.name == "Paladin":
        print("Give me your",char.weapon,"and I will bless it with my magic of my god.")
        input("You gave the 'Old Man' your weapon and after a short chant, it started to glow.")
    else:
        input("If you have any elixers left I would use it when you reach the top.")
    input("Now climb the steps befor this evil spreads though out world!")

def highPoint(char):
    print("The", char.name, "scale the long stair case till the entrance was reached.")
    input("Inside the monster that was terrorize the town was there.")
    print("It was floating in the air,\nwith its legs cross, completly still\nlike it was meditating.")
    print("Its feet replace with hoves, its skin is the color of blood, 2 large horns were on it head and look about 20 feet tall.")
    input("You came face to face with a 'Demon Lord'!\nLucky you didn't notice you so the element of surprise is on your side.")
    demonLordIncounter(char)

def demonLordIncounter(char):
    while True:
        attacks.attackOptions()
        a = input("What should you do: ")

        if a == "1" or a.lower() == "charge":
            print("The", char.name, "charges towards the 'Demon Lord',")
            input("but in that moment, its eye opend before you could touch him")
            game_over.firstStrikeDemon(char, 8)
            break
        elif a == "2" or a.lower() == "shoot":
            if char.name == "Archer":
                print("The", char.name, "fires a arrow at the 'Demon Lord',")
                input("but it only ricochet off it.\nThen its eyes open.")
                game_over.firstStrikeDemon(char, 8)
                break
            else:
                attacks.noProjectile(char)
                continue
        elif a == "3" or a.lower() == "cast":
            if char.name == "Mage" or char.name == "Paladin":
                print("The", char.name, "prepares to cast",char.spell,"on the 'Demon Lord',")
                input("but its eyes open before the spell could be cast.")
                game_over.firstStrikeDemon(char, 8)
                break
            else:
                attacks.noSpells(char)
                continue
        elif a == "4" or a.lower() == "sneak":
            print("The", char.name, "try to sneak up to the 'Demon Lord' but its")
            input("sense was more powerful then most foes and its eyes open.")
            game_over.firstStrikeDemon(char, 8)
            break
        elif a.lower() == "scroll of weakening":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                input("The 'Scroll of Weakening' turn to dust after use.")
                demonLordFight(char)
        elif bag.threeActions(a) == True:
            continue
        else:
            bag.invalid()


def demonLordFight(char):
    global improvedWepon

    print("The 'Demon Lord' roar in pain as it crashs to the ground.\nIt opens its gaze towards the",char.name,"and shown a face of anger and fustraction")
    input("YOU THINK YOU COULD KILL ME WITH THAT PITIFUL MAGIC?\nYOU DIE HERE AND THAT NEST YOU CALLED HOME WILL BE BURNED TO THE GROUND!")
    while True:
        attacks.attackOptions()
        a = input("What should you do: ")

        if a == "1" or a.lower() == "charge":
            if char.name == "Warrior" or char.name == "Paladin":
                print("The", char.name, "charges towards the 'Demon Lord',")
                print("Your",char.weapon,"struck the 'Demon Lord' in the leg")
                if improvedWepon == False:
                    input("but only seems to phase him")
                    game_over.secondStrikeDemon(char, 8)
                    break
                else:
                    print("The damage done to it cuase the 'Demon Lord' to cream as it fell to its knees.")
                    print("You climbed to its back and took you",char.weapon,"to were it heart is.")
                    input("You lost how mnay time you stuck the 'Demon Lord' but enought was enough")
                    game_over.youWin(char)
                    break
            else:
                print("The", char.name, "would charges at the 'Demon Lord',")
                input("but its probably best to use a diffrent tactic.")
                continue
        elif a == "2" or a.lower() == "shoot":
            if char.name == "Archer":
                print("The", char.name, "fires a arrow at the 'Demon Lord',")
                if improvedWepon == False:
                    input("It penetrated its flesh,\nbut didnt even phase it.")
                    game_over.secondStrikeDemon(char, 8)
                    break
                else:
                    print("When it struck its flesh, an explosion cuase the 'Demon Lord' to fall.")
                    print("You then drew another arrow and contiue to fire over, and over, over")
                    input("Till you were out of arrows.")
                    game_over.youWin(char)
                    break
            else:
                attacks.noProjectile(char)
                continue
        elif a == "3" or a.lower() == "cast":
            if char == "Mage" or char == "Paladin":
                print("The", char.name, "casts",char.spell,"on the 'Demon Lord',")
                input("but barly left a mark as the 'Demon Lord' look more angry.")
                game_over.secondStrikeDemon(char, 8)
                break
            else:
                attacks.noSpells(char)
                continue
        elif a == "4" or a.lower() == "sneak":
            if char.name == "Theif":
                print("The", char.name, "vanish into the shadows,\ngot behind the 'Demon Lord',")
                input("and stabe it in the Head.")
                if improvedWepon == False:
                    input("But it only made it more angry.")
                    game_over.secondStrikeDemon(char, 8)
                    break
                else:
                    print("The 'Demon Lord' cry out in pain, but you continue to stab the demon in the head over, and over, and over")
                    input("untill you lost the strength to stabe again.")
                    game_over.youWin(char)
                    break
            else:
                print("The", char.name, "would sneak towards the 'Demon Lord',")
                input("but its probably best to use a diffrent tactic.")
                continue
        elif a.lower() == "elixer of arcan":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                print("The power of arcan fused with your very essence as you cojured a masive",char.spell,"and throw it at the 'Demon Lord'.")
                input("Thought it didn't killed the 'Demon Lord', but it did fell, face first, on the ground.")
                game_over.youWin(char)
                break
        elif a.lower() == "symbol of kings":
            if bag.useItem(a.lower(), char) == False:
                continue
            else:
                print("The wrath of god was summon and your",char.spell,"was cast and the 'Demon Lord' scream from it heavenly burn")
                input("It then fell, face first, on the ground.")
                break
        elif bag.threeActions(a) == True:
            continue
        else:
            bag.invalid()
