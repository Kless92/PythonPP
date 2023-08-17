from pp_pkg import town_interiors, forest, marshes, mountains
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
            elif num == 6:
                marshes.necroDeath(char)
            elif num == 7:
                marshes.largeStump(char)
            elif num == 8:
                mountains.mountains(char)
        elif a.lower() == "n" or a.lower() == "no":
            quit()
        else:
            print("Not a vaild input!")


def rejectJob(char):
    print("The",char.name," rejected the contract and left the small town.")
    print("You later learn that the mysteries monster has destory it and it inhabitants.")
    input("Could you have done something about it? Who knows now.")
    choice(char, 1)
    
def arrowFlys(char):
    print("Before the",char.name,"could do anything else, a sharp pierce penetrated thought the chest.")
    input("Blood fill the lunges and the vision begian to blure\nuntil finally death took the last breath was drawn.")
    choice(char, 2)

def failedCharge(char, number):
    print("The",char.name,"charge towards the enemy and failed.")
    input("You were ripped appart untill death finally end your suffering.")
    choice(char, number)
    
def sneakFailed(char, number):
    print("The",char.name,"tryied to sneak over but failed.")
    input("The deatils are unknow but you death was very painfull.")
    choice(char, number)

def necroCharge(char, number):
    print("The",char.name,"charge the 'Necro Manser'\nbut he notice you before you could reach him. ")
    necroBlast(char, number)

def necroShoot(char, number):
    print("The",char.name,"fired a arrow at the 'Necro Manser',\nbut he suddenly vanish as the arrow flew into wall.")
    print("You saw the 'Necro Manser' on the right of the room.")
    input("And he then struck back.")
    necroBlast(char, number)

def necroCast(char, number):
    print("The",char.name,"cast",char.spell,"at the 'Necro Manser' but it was absorbed by a magic sheild")
    input("You think im some novice? How pathetic.")
    necroBlast(char.name, number)

def necroSneak(char, number):
    print("The",char.name,"sneak twords the 'Necro Manser' but suddenly froze soild.\nIt was a trad")
    input("The 'Necro Manser' turn, shock, but then start laughing maniacally.")
    choice(char, number)

def necroBlast(char, number):
    print("He then cast a spell on the",char.name)
    input("who was turned into a walking corpse")
    choice(char, number)

def witchCurse(char, number):
    print("The",char.name,"turned into a frog.")
    input("Now the Witch will have frog stew tonight.")
    choice(char, number)

def firstSrikeDemon(char, number):
    print("You think you could touch me with you moratl hands?")
    print("The 'Demon Lords' eyes gaze on the",char.name,"and was trun into a pile of dust.")
    input("Never stood a chance")
    choice(char, number)