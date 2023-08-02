from pp_pkg import town

def theCrossRoads(char):        
    print("1.) Mountans\n2.) Forest\n3.) Marshes\n4.) Cemetery\n5.) Town")
    
    a = input("Were do u want to go: ")

    while True: 
        if a == '5':
            town.welcomeToTown(char, False)
            break
        else:
            print()