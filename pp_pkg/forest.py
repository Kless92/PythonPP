from pp_pkg import cross_roads, bag

forestFirst = True

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

def intoLostForest(char):
    print(char)

def invTheLeft(char):
    print(char)
        