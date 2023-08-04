from pp_pkg import town, bag

crossRoadsFirst = True

def theCrossRoads(char):  
    global crossRoadsFirst
    b = "map"
    if crossRoadsFirst == True:
        print("The",char,"travel over an hour till eventually reached a cross roads.\nSouth would obviously take the",char,"back to town.")
        input("But were the others would take is unknown.")
    else:
        print("The",char,"return to the cross roads")
        input("once again.") 
    crossRoadsFirst = False

    while True: 
        print("1.) North\n2.) West\n3.) East\n4.) South")
        if "map" in bag.bag:
            print("5.) Map")
        a = input("Were do u want to go: ")
        if bag.checkBag(a) == True:
            continue
        if "map" in bag.bag:
            if bag.checkMap(a) == True:
                continue
        if a == "1":
            print()
        elif a == "2":
            print()
        elif a == "3":
            print()
        elif a == '4':
            town.welcomeToTown(char, False)
            break
        else:
            print("Not a vaild Input.")

