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
    if a.lower() == "h" or a.lower() == "help":
        print("Type b or bag to check your inventory")
        print("Type name of a item to use it")
        print("Type 1-9 if the options have numbers on it or its name, 1 or 2 words")
        print("Type y or n for yes or no.")
        print("Type words like question, ask, monster, buy or supplies")
        print("Type exit or leave to exit current location")
        input("Look for quotes on key words.")
        return True
    
#Repeat of Invalid inputs
def invalid():
    input("Not a vaild input please type 1-5 or the name as one of two words.")

#If map is in you bag, then discription is be printed out
def checkMap(a, atCrossRoads):
    if a.lower() == "map":
        if "map" not in bag:
            invalid()
        elif atCrossRoads == True:
            print("On the map you see A 'Cross Roads' in the center.\nTo the North are Mountains.")
            input("West is the Lost Forest.\nEast the Marsh Lands.\nAnd South the Town.")
        else:
            input("Theres no reason to use that right now.")
        return True
        
#useitem
def useItem(a, char):
    if a in bag:
        print(char.name,"used",a,".")
        bag.remove(a)
    else:
        print(a,"isn't in you bag.")
        return False
    
def threeActions(a, b):
    if helpMe(a) == True:
        return True
    if checkBag(a) == True:
        return True
    if checkMap(a, b) == True:
        return  True