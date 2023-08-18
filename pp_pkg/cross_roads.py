from pp_pkg import marshes, town, forest, mountains, bag

crossRoadsFirst = True
doneWithForest = False
doneWithMarshes = False

def theCrossRoads(char):  
    global crossRoadsFirst, doneWithForest, doneWithMarshes

    if crossRoadsFirst == True:
        print("The",char.name,"travel over an hour till eventually reached a 'Cross Roads'.\nSouth would obviously return you back to town.")
        input("But were the others would take is unknown.")
        crossRoadsFirst = False
    else:
        print("The",char.name,"return to the 'Cross Roads',")
        input("once again.") 


    while True: 
        print("1.) North\n2.) West\n3.) East\n4.) South")
        a = input("Were do u want to go: ")

        if a == "1" or a.lower() == "north":
            mountains.mountains(char)
            break
        elif a == "2" or a.lower() == "west":
            if doneWithForest == True:
                input("No reason to go there anymore.")
                continue
            else:
                forest.lost_forest(char)
                break
        elif a == "3" or a.lower() == "east":
            if doneWithMarshes == True:
                input("No reason to go there anymore.")
                continue
            else:
                marshes.marshLands(char)
                break
        elif a == '4' or a.lower() == "south":
            town.welcomeToTown(char, False)
            break
        elif a.lower() == "map":
            bag.checkMap()
            break
        elif bag.threeActions(a) == True:
            continue
        else:
            bag.invalid()

