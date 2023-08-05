from pp_pkg import town_interiors, cross_roads, bag

def welcomeToTown(char, bool):
    if bool == True:
        print("The", char,
              "came to a small town.\nThought the sun is height, it looks and feels empty.\nMost are inside look thought the windows.")
        input("You heard rumor of a 'monster' picking off travler close by so. \nIt would be easy money, should head to the 'Town Hall'.")
    else:
        print("The", char, "return to the small town.")

    while True:
        print("You see the\n1.) Town Hall\n2.) General Store\n3.) Magic Shop\n4.) Inn\n5.) Church\n6.) Exit Town")
        a = input("Were do you want to go first: ")

        if bag.checkBag(a) == True:
            continue
        if bag.helpMe(a) == True:
            continue

        if a == "1" or a.lower() == "town hall" or a.lower() == "townhall":
            town_interiors.townHall(char)
            break
        elif a == "2" or a.lower() == "general store" or a.lower() == "generalstore":
            town_interiors.generalStore(char)
            break
        elif a == "3" or a.lower() == "magic shop" or a.lower() == "magicshop":
            town_interiors.magicShop(char)
            break
        elif a == "4" or a.lower() == "inn":
            town_interiors.inn(char)
            break
        elif a == "5" or a.lower() == "church":
            town_interiors.church(char)
            break
        elif a == "6" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break
        else:
            input("not a vaild input please type 1-5 or the name as one of two words.")
