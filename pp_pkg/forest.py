from pp_pkg import cross_roads, bag

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
    print(char)

def invTheLeft(char):
    global investFirst

    print("The",char,"walked into a small camp.")
    input("It looks almost new.\nShould look more closely into it.")

    while True:
        print("1.) Investigate the camp.\n2.) Leave the camp.")
        a = input("What should you do: ")
        if a == "1" or a.lower() == "investigate" or a.lower() == "camp":
            if investFirst == True:
                print("In the center is a fire that died some time ago.")
                print("Discared food and what looks like two bodies sleaped on.\nThe foot print look like 1 human and one animal;\nmost likly a dog.")
                input("There was also seems to be a scuffle as were they rest have movement around.\nMost likly something work them up.")
                print("Near it the",char,"Notice a bandage, most likly the hunter dropped it. So the",char,"took it.")
                input("Probbly going to need it.")
                bag.bag.append("Bandage")
                input("You picked up a Bandage.")
                investFirst = False
            else:
                print("The",char,"already looked over the camp.")
                input("Nothing has changed.")
        elif a == "2" or a.lower() == "exit" or a.lower() == "leave":
            lost_forest(char)
            break
        else:
            input("Not a valid input.")
        