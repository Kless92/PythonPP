from pp_pkg import town_interiors
def choice(char, num):
    while True:
        a = input("Do you wish to continue: ")
        if a.lower() == "y" or a.lower() == "yes":
            if num == 1:
                town_interiors.townHall(char)
        elif a.lower() == "n" or a.lower() == "no":
            quit()
        else:
            print("Not a vaild input!")


def rejectJob(char):
    print("The",char," rejected the contract and left the small town.")
    print("You later learn that the mysteries monster has destory it and it inhabitants.")
    input("Could you have done something about it? Who knows now.")
    choice(char, 1)