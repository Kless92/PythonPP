from pp_pkg import town_interiors, cross_roads, bag
gotItems = False

def welcomeToTown(char, firstTime):
    global gotItems

    if firstTime == True:
        print("The", char.name,"arrive at a small town.\nThought the sun was height, it looks and feels empty.")
        print("Most of the towns folk were inside look thought their windows.\nYou heard rumor of a 'Monster' picking off travler close by so.")
        input("Killing this 'Monster' might be easy money, should head to the 'Town Hall'.")
    else:
        print("The", char.name, "returns to the small town.")

    while True:
        print("You see the\n1.) Town Hall\n2.) General Store\n3.) Magic Shop\n4.) Inn\n5.) Church\n6.) Exit Town")
        a = input("Were do you want to go first: ")


        if a == "1" or a.lower() == "town hall" or a.lower() == "townhall":
            town_interiors.townHall(char)
            break
        elif a == "2" or a.lower() == "general store" or a.lower() == "generalstore":
            if goToTownHall(firstTime) == True:
                continue
            town_interiors.generalStore(char)
            break
        elif a == "3" or a.lower() == "magic shop" or a.lower() == "magicshop":
            if goToTownHall(firstTime) == True:
                continue
            town_interiors.magicShop(char)
            break
        elif a == "4" or a.lower() == "inn":
            if goToTownHall(firstTime) == True:
                continue
            town_interiors.inn(char)
            break
        elif a == "5" or a.lower() == "church":
            if goToTownHall(firstTime) == True:
                continue
            town_interiors.church(char)
            break
        elif a == "6" or a.lower() == "exit" or a.lower() == "leave":
            if goToTownHall(firstTime) == True or getSomeThings(gotItems) == False:
                continue
            cross_roads.theCrossRoads(char)
            break
        elif bag.threeActions(a) == True:
            continue
        else:
            bag.invalid()

def goToTownHall(firstTime):
    if firstTime == True:
        input("You should go to the Town Hall first.")
        return True
    else:
        return False

def getSomeThings(items):
    if items == False:
        input("You should get some supplies first.")
        return False
    else:
        return True
