from pp_pkg import cross_roads, bag

marcehsFirst = True

def marchLands(char):
    global marcehsFirst

    if marcehsFirst == True:
        input()
        marcehsFirst = False
    else:
        input()
    
    while True:
        print("1.) Go to the Crypt\n2.) Head to the Old Shak.\n3.) Head tword the Large Trunk.\n4.) Leave the area")
        a = input("What should you do: ")

        if a == "1" or a.lower() == "crypt":
            theCrypt(char)
        elif a == "2" or a.lower() == "shak" or a.lower() == "old shak" or a.lower() == "oldshak":
            oldShak(char)
        elif a == "3" or a.lower() == "trunk" or a.lower() == "large trunk" or a.lower() == "largetrunk":
            largeTrunk(char)
        elif a == "4" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break

def theCrypt(char):
    print(char)

def oldShak(char):
    print(char)

def largeTrunk(char):
    print(char)