from pp_pkg import town, game_over


def townHall(char):

    print("The", char, "enter the Town Hall and notice a anxious large man pascing around mubbling to himself.")
    print("The large man notice the", char,
          ", given a suprice and then a excited look.")
    input("Please come over I wish to speak with you!")
    print("You timming couldn't be anymore perfice.  I can tell that you the adventuring kind and I happen to have a bounty for you.")
    print("Theres a Monster that lives North of here and has ben tarizing this community for too long.")
    print("So I ask you", char, ". Would you help us?")
    while True:
        a = input("What should you do: ")

        if a.lower() == 'y' or a.lower() == 'yes':
            print("That excelent!  I knew you would say that the moment I layed eyes on you.")
            input("Now if there anything more you need just ask away.")
            break
        elif a.lower() == 'n' or a.lower() == 'no':
            print("Oh I see, I was wrong about you. Well",char,".")
            input("I recommend that you leave this town before it too late.")
            game_over.rejectJob(char)
            break
        else:
            print("I dont undersatnd?  You you help us or not?")
    while True:
        print("1.) Ask about the monster.\n2.) Were is this monster again.\n3.) Return to the town.")
        a = input("What should you do: ")
        if a.lower() == '1' or a.lower() == 'ask' or a.lower() == 'question':
            print()
        elif a.lower() == '2':
            print()
        elif a.lower() == '3':
            town.welcomeToTown(char, False)
        else:
            input("Not a valid input.")


def generalStore(char):
    print("generalStore function has been called:", char)


def magicShop(char):
    print("magicShop function has been called:", char)


def inn(char):
    print("inn function has been called:", char)


def church(char):
    print("church function has been called:", char)
