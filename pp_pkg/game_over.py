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

def firstStrikeDemon(char, number):
    print("You think you could touch me with you moratl hands?")
    demonKills(char, number)

def secondStrikeDemon(char, number):
    print("You think im that weak mortal?\nNow you will know pain!")
    demonKills(char, number)

def demonKills(char, number):
    print("The 'Demon Lords' release a pulse of energy towards the",char.name,"and was trun into a pile of dust.")
    input("Never stood a chance")
    choice(char, number)
def youWin(char):
    print("The 'Demon Lord' was laying on the ground, completly void of life.\nYou have successfully killed the target")
    print("The",char.name,"remove the 'Demon Lord's head from its shoulder")
    input("and drag it from the top of the mountain back to town")
    print("It was Twilight when you return to town and the residence left ther home to see the",char.name,"kill.")
    input("Even the mayor run out and was shocked to see you exploits.")
    print("WELL DONE, he shouted, I had no idea it was a 'Demon Lord'\nand you were still able to kill it.")
    print("You have done this town a great favor",char.name,".")
    print("Here is the reward promissed and why dont you stay were all going to celebrate,")
    input("the entire town want to thank you for you efferts.")
    input("But you weren't intrested, you simply took the money and left the town.")
    print("The",char.name,"can here fire work from the Town,\nmaking you wonder if they turly ran out of supplies?")
    print("But it doesn't matter, you got the gold from a job.\nA difficult job, but on none the less.")
    input("Now you off to the next adventure.")
    thankYou()
    
def thankYou():
    print("Thank you for playing my Portfolio Project.\nPlease let me know what you think\nor if there any issues you encountered.")
    input("Type python main.py to play again.")
    quit()

    