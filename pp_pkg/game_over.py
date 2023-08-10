from pp_pkg import town_interiors, forest, marshes
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
            elif num == 4:
                marshes.theCrypt(char)
            elif num == 5:
                marshes.necroFight(char)
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

def necroCharge(char, number):
    print("The",char,"charge the Necro Manser\nbut he notice you before you could reach him. ")
    necroBlast(char, number)

def necroShoot(char, number):
    print("The",char,"fired a arrow at the Necro Manser,\nbut he suddenly vanish as the arrow flew into wall.")
    print("The",char,"saw the Necro Manser on the right of the room,\nthe",char,"was too slow to draw another arrow.")
    input("For the Necro Mancer struck back.")
    necroBlast(char, number)

def necroCast(char, number):
    print("The",char,"cast a spell at the Necro Manser but it was absorbed by a magic sheild")
    input("You think im some novice? How pathetic.")
    necroBlast(char, number)

def necroSneak(char, number):
    print("The",char,"sneak twords the Necro Manser but suddenly froze soild.\nIt was a trad")
    input("The Necro Manser turn, shock, but then start laughing maniacally.")
    choice(char, number)

def necroBlast(char, number):
    print("He then cast a spell and on the",char)
    input("who is now a walking corpse")
    choice(char, number)