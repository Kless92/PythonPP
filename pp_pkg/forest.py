from pp_pkg import cross_roads, bag, game_over, attacks

forestFirst = True
investFirst = True

def lost_forest(char):
    global forestFirst

    if forestFirst == True:
        print("The",char.name,"stood at the entrance of the Lost Forest")
        print("Infront of the you is a long path that leads deeper into the Lost Forest.")
        print("But you notices some thing to the left.")
        input("Should probally investigate.")
        forestFirst = False
    else:
        print("The",char.name,"returns to the entrance,")
        input(" of the 'Lost Forest'.")
    
    while True:
        print("1.) Go into the Lost Forest\n2.) Head left to investigate.\n3.) 'Leave' the area")
        a = input("What should you do: ")
        if bag.threeActions(a, False) == True:
            continue
        if a == "1" or a.lower() == "go" or a.lower() == "enter":
            intoLostForest(char)
        elif a == "2" or a.lower() == "left" or a.lower() == "investigate":
            invTheLeft(char)
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break
        else:
            bag.invalid

def intoLostForest(char):
    print("Into the forest the",char.name,"enter. \nAfter some time pass, moving deeper in,\nvisiablity from a distance became almost impossible.")
    input("You now see why the forst got its name.\nPerhaps the 'Huntsmen' has already left the forest and return to town.")
    input("DONT TAKE ANOTHER STEP!")

    while True:
        a = input("Should you 'stop' or keep moving.")
        if a.lower() == "stop":
            print("You stood completly still while the sounds of foot step were getting closer and closer.")
            print("Now the",char.name,"can see a tall crimson hair man with his bow drawn toward you.")
            input("Its the 'Huntsmen'.")
            print("Whats a",char.name,"doing in the Lost Forest?")
            input("Speak quickly!")
            print("You explained everything about your job.")
            input("I see, the 'Huntsmen' as he lowered his bow.")
            print("Well I seen the monster and it worse then the rumors throughout town.")
            input("But if you want to know what your going up aginst, you need to do something for me.")
            print("My dog ran off  into the forest not too long ago and I need to find him.")
            input("Come along and help me out.")
            battleOfWolves(char)
            break
        else:
            game_over.arrowFlys(char)

def invTheLeft(char):
    global investFirst

    print("The",char.name,"walks into a small camp.")
    input("It looks almost new.\nShould look more closely into it.")

    while True:
        print("1.) Investigate the camp.\n2.) 'Leave' the camp.")
        a = input("What should you do: ")
        if bag.threeActions(a, False) == True:
            continue
        if a == "1" or a.lower() == "investigate" or a.lower() == "camp":
            if investFirst == True:
                print("In the center is a fire that died out some time ago.")
                print("Discared food and what looks like two prints were bodies sleeped on.")
                print("Also two sets of foot print.\nOne that looks human and an animal;\nmost likly a dog.")
                input("Both trails off into the 'Lost Forest'.")
                print("You then notice a bandage on the ground, most likly the 'Huntsmen' dropped it in a hurry.")
                input("Probbly going to need it.")
                bag.bag.append("bandage")
                input("You picked up a Bandage.")
                investFirst = False
            else:
                print("The",char.name,"already looked over the camp again.")
                input("Nothing has changed.")
        elif a == "2" or a.lower() == "exit" or a.lower() == "leave":
            lost_forest(char)
            break
        else:
            bag.invalid()
        
def battleOfWolves(char):
    print("Time pass again after the",char.name,"found the 'Huntmen'.\nEventually a large patch of light appared at last.")
    input("They then heard the sound of wimpering, so the the 'Huntsmen' ran twords the sound and you followed.")
    input("Through the light it was a large tree with the sun beaming on it, and under the tree was the injered dog, surrounded by wolves.")
    print("Listen here",char.name,".\nThat my girl and I'm not going to let her get eaten by that pack.")
    print("So heres whats goign to ahppen.\nYou kill one of them and I'll shoot one another.\nWhen both are dead the last one will run away.")
    input("Go when your ready, but hurry.")
    
    while True:
        attacks.attackOptions()
        a = input("What should you do:")
        if bag.threeActions(a, False) == True:
            continue
        if a == "1" or a.lower() == "charge":
            if char.name == "Warrior":
                print("The",char.name,"charge on of the wolves.")
                print("Crushing it with your",char.weapon,".")
                input("The wolf is now dead.")
                break
            elif char == "Paladin":
                print("The",char,"charge on of the wolves.")
                print("Sliceing it in half with your",char.weapon,".")
                input("The wolf is now dead.")
                break
            else:
                game_over.failedCharge(char, 3)
        elif a == "2" or a.lower() == "shoot":
            if char.name == "Archer":
                print("The",char.name,"fired a arrow at one of the wolves head.")
                input("Killing it in one perfict shoot.")
                break
            else:
                attacks.noProjectile(char)
                continue
        elif a == "3" or a.lower() == "cast":
            if char.name == "Mage":
                print("The",char.name,"cast a",char.spell,"at one of the wolves.")
                input("Turning it into a pile of ash.")
                break
            elif char.name == "Paladin":
                print("The",char.name,"cast",char.spell,"at one of the wolves.")
                input("Cause the wolf to howell in pain as it runs away.")
                break
            else:
                attacks.noSpells(char)
                continue
        elif a == "4" or a.lower() == "sneak":
            if char.name == "Theif":
                print("The",char.name,"snuck twords one of the wolves.")
                print("Before the wolfe notice, it was stabe in the heart.")
                input("Giving it a quick death.")
                break
            else:
                game_over.sneakFailed(char, 3)
        else:
            bag.invalid()
    
    print("The 'Huntsmen' shoot the other wolf and the soul survivor run into the forest.")
    print("Both the",char.name,"and 'Huntsmen' run the the injured dog.")
    input("DAMN!")
    print("I dont have my 'bandage'. I must have droped it back at camp!")
    print(char.name,"please help her!")
    
    while True:
        a = input("What should you do:")

        if a.lower() == "bandage":
            if bag.useItem(a.lower(), char) == False:
                continue
            
        elif a.lower() == "potion":
            if bag.useItem(a.lower(), char) == False:
                continue
            
            print("You gave the 'Huntsmen' the",a.lower(),"as he used it immediately on his dog.")
            print("The dogs wimpering stopped and her breathing slown")
            input("YOU SAVED HER, THANK YOU!\nThank you so much!")
            print("Now you probly want to know about the monster attacking travlers but no one knows what it looks like.\nWell it not a monster from this world, its a 'Demon Lord'.")
            input("I seen it myself and it a hug.")
            print("And no disrespect but I dont you can kill this 'Demon Lord' not with what you have right now.\nI think theirs somoneone who can help.")
            input("In the 'Marsh Lands', east of the 'Cross Roads' is a 'Shack' and living in it is a 'Old Women'.\nI think she'll be able to help you more then I can.")
            if char.name == "Archer":
                print("Also seeing that your a",char.name,"and that you saved my dog,")
                input("I wanted to give you this.")
                bag.bag.append("black arrow")
                input("You were givin a Black Arrow")
            input("You better head out now before the 'Demon Lord' attacks again and good luck to you.")
            print("So the",char.name,"leave the 'Huntsmen' with his dog, happy as a man and his best friend would be.")
            print("Leaving the 'Lost Forest' the",char.name,"learn that the 'monster' is a 'Demon Lord'.")
            input("Could this 'Old Wemon' really be of help?")
        else:
            print("The",char.name,"did nothing and the dog die.")
            input("YOU BASTARED!\nYOU KILLED HER!\nGET OUT OF MY SIGHTS!\nIF I SEE YOU EVER AGAIN, I'LL KILL YOU MYSELF")
            print("The",char.name,"left the 'Huntsmen' also with his dead dog.")
            input("Leaving the 'Lost Forest' gaining nothing for this incounter.")
        cross_roads.doneWithForest = True
        cross_roads.theCrossRoads(char)