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
        print("Type b or bag to check your inventory.")
        print("Type name of a item to use it.")
        print("Type 1-9 if the options have numbers on it or its name, 1 or 2 words.")
        print("Type y or n for yes or no.")
        print("Type words like question, ask, monster, buy or supplies.")
        print("Type exit or leave to exit current location.")
        print("Some items can be used in certain location or scenarios.")
        input("Look for quotes on key words.")
        return True
    
#Repeat of Invalid inputs
def invalid():
    input("Not a vaild input please type 1-5 or the name as one of two words.")

#Prevent item from being used    
def cantBeUsed(a):
    if a in bag:
        print(a,"can't be used,")
        input("at this time.")
        return True
    else:
        return False 
    
#useitem
def useItem(a, char):
    if a in bag:
        print(char.name,"used",a,".")
        bag.remove(a)
    else:
        print(a,"isn't in you bag.")
        return False  

#function for checking on the map, if the user has it and is @ cross roads
def checkMap():
    print("On the map you see A 'Cross Roads' in the center.\nTo the North are Mountains.")
    input("West is the Lost Forest.\nEast the Marsh Lands.\nAnd South the Town.")

#A function that hold 3 diffrent funcitons for optimization     
def threeActions(a):
    if helpMe(a) == True:
        return True
    if checkBag(a) == True:
        return True
    if cantBeUsed(a) == True:
        return True