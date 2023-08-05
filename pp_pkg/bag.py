bag = []
#Check for items in your bag
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
    
#Give tip for what to input
def helpMe(a):
    if a.lower() == "help":
        print("Type b or bag to check your inventory")
        print("Type 1-9 if the options have numbers on it or its name, 1 or 2 words")
        print("Type y or n for yes or no.")
        print("Type words like question, ask, monster, buy or supplies")
        print("Type exit or leave to exit current location")
        input("Look for quotes on key words.")
        return True

#If map is in you bag, then discription is be printed out
def checkMap(a):
    if a == "5" or a.lower() == "map":
        if "map" in bag:
            print("On the map you see A Cross Roads in the center.\nTo the North are Mountains.")
            input("West is the Lost Forest.\nEast the Mash Lands.\nAnd South the Town.")
            return True
        else:
            return False