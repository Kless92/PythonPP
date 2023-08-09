from pp_pkg import cross_roads, bag, game_over

forestFirst = True
investFirst = True

def lost_forest(char):
    global forestFirst

    if forestFirst == True:
        print("The",char,"stood at the entrance of the Lost Forest")
        print("Infront of the",char,"is a long path that leads deeper into the Lost Forest.")
        print("But the",char,"notices some thing to the left.")
        input("Should probally investigate.")
        forestFirst = False
    else:
        print(char,"returns to the entrance,")
        input("of the Lost Forest.")
    
    while True:
        print("1.) Go into the Lost Forest\n2.) Head left to investigate.\n3.) Leave the area")
        a = input("What should you do: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a == "1" or a.lower() == "go" or a.lower() == "enter":
            intoLostForest(char)
        elif a == "2" or a.lower() == "left" or a.lower() == "investigate":
            invTheLeft(char)
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break
        else:
            input("Not a valied input.")

def intoLostForest(char):
    print("Into the forest the",char,"enter. \nAfter some time pass, moving deeper in,\nvisiablity from a distance became almost impossible.")
    print("Now the",char,"see why the forst got its name.")
    input("Perhaps the hunter already left the forest.")
    print("DONT TAKE ANOTHER STEP!")

    while True:
        a = input("Should you 'stop' or keep moving.")
        if a.lower() == "stop":
            print("Completely still the",char,"stood while the foot step was getting closer.")
            print("Now the",char,"can see a tall crimson hair man with his bow drawn toward you.")
            input("Its the hunter.")
            print("Whats a",char,"doing in the Lost Forest?")
            input("Speak quickly!")
            print("The",char,"explained everything with the job you got.")
            input("I see, said hunter as he lowered his bow.")
            print("Well I seen the monster and it worse then we thought.")
            input("But if you want to know what your going up aginst, you need to do something for me.")
            print("My dog ran off not too long ago into the forest and I need to find him.")
            input("Come along if you want my help.")
            battleOfWolves(char)
            break
        else:
            game_over.arrowFlys(char)

def invTheLeft(char):
    global investFirst

    print("The",char,"walked into a small camp.")
    input("It looks almost new.\nShould look more closely into it.")

    while True:
        print("1.) Investigate the camp.\n2.) Leave the camp.")
        a = input("What should you do: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a == "1" or a.lower() == "investigate" or a.lower() == "camp":
            if investFirst == True:
                print("In the center is a fire that died some time ago.")
                print("Discared food and what looks like two bodies sleaped on.\nThe foot print look like 1 human and one animal;\nmost likly a dog.")
                input("There was also seems to be a scuffle as were they rest have movement around.\nMost likly something work them up and they moved in a hurry.")
                print("You then notice a bandage on the ground, most likly the hunter dropped it. So the",char,"took it.")
                input("Probbly going to need it.")
                bag.bag.append("bandage")
                input("You picked up a Bandage.")
                investFirst = False
            else:
                print("The",char,"already looked over the camp.")
                input("Nothing has changed.")
        elif a == "2" or a.lower() == "exit" or a.lower() == "leave":
            lost_forest(char)
            break
        else:
            bag.invalid()
        
def battleOfWolves(char):
    print("Time pass again after the",char,"found the hunter.\nEventually a large patch of light appared and in the center was a large tree and the sounds of wimpering.")
    input("The hunter rant twords the sound as you followed.\nUnder the tree was the dog, who was injered and surrounded by wolves.")
    print("Ok",char,"listen.  I shoot one on the left you take the one on the right.\nIf both die then the last will run away.")
    input("You go in and I'll fallow now hurry.")
    
    while True:
        print("1.) Charge\n2.) Shoot\n3.) Cast\n4.) Sneak\n5.) Do Nothing")
        a = input("What should you do:")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if a == "1" or a.lower() == "charge":
            if char == "Warrior":
                print("The",char,"charge on of the wolves.")
                input("Crushing it with a Great Hammer")
                break
            elif char == "Paladin":
                print("The",char,"charge on of the wolves.")
                input("Sliceing it in half with a Great Sword.")
                break
            else:
                game_over.failedCharge(char, 3)
        elif a == "2" or a.lower() == "shoot":
            if char == "Archer":
                print("The",char,"fired a arrow at one of the wolves head.")
                input("Killing it in one perfict shoot.")
                break
            else:
                print("The",char,"doesn't have any projectile weapon.")
                input("So nothing happen.")
                continue
        elif a == "3" or a.lower() == "cast":
            if char == "Mage":
                print("The",char,"cast a fire ball at one of the wolves.")
                input("Turning it into a pile of ash.")
                break
            elif char == "Paladin":
                print("The",char,"cast Searing Smite at one of the wolves.")
                input("Cause the wolf to howell in pain as it runs away.")
                break
            else:
                print("The",char,"doesn't know nay spells")
                input("So nothing happen.")
                continue
        elif a == "4" or a.lower() == "sneak":
            if char == "Theif":
                print("The",char,"snuck twords one of the wolves.")
                print("Before the wolfe notice, it was stabe in the heart.")
                input("Giving it a quick death.")
                break
            else:
                game_over.sneakFailed(char, 3)
    
    print("The hunter shoot the other wolf and the soul survivor run into the forest.")
    print("Both the",char,"and hunter run the the injured dog.")
    input("DAMN!")
    print("I dont have my 'bandage'. I must have droped it!")
    print(char,"please help her!")
    
    while True:
        a = input("What should you do:")

        if a.lower() == "bandage":
            if bag.useItem(a.lower(), char) == False:
                continue
            print("The dogs wimpering stopped and her breathing slown")
            print("YOU SAVED HER, THANK YOU!\nThank you so much",char,".")
            print("Now you probly want to know about the monster.\nWell it not a monster, its a 'Demon Lord'.")
            input("I seen it myself and it a hug one.")
            print("And seeing that your up aginst a 'Demon Lord' I think theirs something that can kill it.")
            print("In the 'March Lands', east of the 'cross roads' a large tree stomp and under it is a chest")
            input("Now I dont know whats in it, mostly because I can't open it,\nbut I belive the a old 'Hermit' hiding in the 'shake' in the 'March Lands' might help you with that.")
            if char == "Archer":
                print("I can but help notice your a",char,"and seeing how you saved my dog,")
                input("I wanted to give you this.")
                bag.bag.append("black arrow")
                input("You were givin a Black Arrow")
            input("You better head out now before the 'Demon Lord' attacks again and good luck to you.")
        else:
            print("The",char,"did nothing and the dog die.")
            input("YOU BASTARED!\nYOU KILLED HER!\nGET OUT OF MY SIGHTS!\nI NEVER WANT TO SEE YOU AGAIN")
        cross_roads.doneWithForest = True
        cross_roads.theCrossRoads(char)