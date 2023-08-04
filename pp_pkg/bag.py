bag = []

def checkBag(a):
    if a.lower() == "b" or a.lower() == "bag":
        print("You check inside you bag: ")
        if not bag:
            input("You bag is empty!")
        else:
            for i in bag:
                print(i)
            input()
        return True

def checkMap(a):
    if a == "5" or a.lower() == "m" or a.lower() == "map":
        if "map" in bag:
            print("On the map you see A Cross Roads in the center.\nTo the North are Mountains.")
            input("West is the Lost Forest.\nEast the Mash Lands.\nAnd South the Town.")
            return True
        else:
            return False