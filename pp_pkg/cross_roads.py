from pp_pkg import town, forest, bag

crossRoadsFirst = True

def mapCheck():
    if "map" in bag.bag:
        return True

def theCrossRoads(char):  
    global crossRoadsFirst

    if crossRoadsFirst == True:
        print("The",char,"travel over an hour till eventually reached a cross roads.\nSouth would obviously take the",char,"back to town.")
        input("But were the others would take is unknown.")
    else:
        print("The",char,"return to the cross roads")
        input("once again.") 
    crossRoadsFirst = False

    while True: 
        print("1.) North\n2.) West\n3.) East\n4.) South")
        if mapCheck() == True:
            print("5.) Map")
        a = input("Were do u want to go: ")
        if bag.helpMe(a) == True:
            continue
        if bag.checkBag(a) == True:
            continue
        if mapCheck() == True:
            if bag.checkMap(a) == True:
                continue
        if a == "1" or a.lower() == "north":
            print()
        elif a == "2" or a.lower() == "west":
            forest.lost_forest(char)
            break
        elif a == "3" or a.lower() == "east":
            print()
        elif a == '4' or a.lower() == "south":
            town.welcomeToTown(char, False)
            break
        else:
            print("Not a vaild Input.")

