from pp_pkg import town_interiors, forest
def choice(char, num):
    while True:
        a = input("Do you wish to continue: ")
        if a.lower() == "y" or a.lower() == "yes":
            if num == 1:
                town_interiors.townHall(char)
            elif num == 2:
                forest.intoLostForest(char)
            elif num == 3:
                forest.battleOfWolves(char)
        elif a.lower() == "n" or a.lower() == "no":
            quit()
        else:
            print("Not a vaild input!")


def rejectJob(char):
    print("The",char," rejected the contract and left the small town.")
    print("You later learn that the mysteries monster has destory it and it inhabitants.")
    input("Could you have done something about it? Who knows now.")
    choice(char, 1)
    
def arrowFlys(char):
    print("Before the",char,"could do anything else, a shar pierce penetrated thought the chest.")
    print("Blood fill the lunges and the vision begian to blure until finally death took the",char,".")
    input("Rest in piece")
    choice(char, 2)

def failedCharge(char, number):
    print("The",char,"Charge into the enemy and failed.\nRipped appart the,",char,"felt,")
    input("untill death finally relase thee from suffering.")
    choice(char, number)
    
def sneakFailed(char, number):
    print("The",char,"tryied to sneak over but failed.")
    input("The deatils are unknow but lets assume the was painfull death.")
    choice(char, number)