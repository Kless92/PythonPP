from pp_pkg import cross_roads, bag

mountFirst = True

def mountains(char):
    global mountFirst

    if mountFirst == True:
        input()
        mountFirst = False
    else:
        input()
    
    while True:
        print("1.) Go up to High Point\n2.) Head towards the Low Cave.\n3.) Take the Odd Path\n4.) 'Leave' the area")
        a = input("What should you do: ")

        if a == "1" or a.lower() == "go" or a.lower() == "enter":
            highPoint(char)
        elif a == "2" or a.lower() =="cave" or a.lower() == "low cave" or a.lower() == "lowcave":
            lowCave(char)
        elif a == "3" or a.lower() =="left" or a.lower() == "path"or a.lower() == "odd path" or a.lower() == "oddpath":
            oddPath(char)
        elif a == "4" or a.lower() == "exit" or a.lower() == "leave":
            cross_roads.theCrossRoads(char)
            break
def highPoint(char):
    print(char)

def lowCave(char):
    print(char)

def oddPath(char):
    print(char)