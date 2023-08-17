from pp_pkg import town, game_over, bag
# Varable to prevent repeating lines
townHallFirst = True
generalStoreFirst = True
magicShopFirst = True
innFirst = True
churchFirst = True
generalSupp = True
magicSupp = True
theifSupp = True
churchSupp = True
innRumor = True
theifInfo = True

# Town Hall fucntion
def townHall(char,):
    global townHallFirst

    if townHallFirst == True:
        print("The", char.name, "enter the Town Hall and notice a anxious large man paceing around mubbling to himself.")
        print("The large man notice the", char.name,", given a suprice and then excited look.")
        input("Please come over I wish to speak with you!")
        print("You timming couldn't be anymore perfice.  I can tell that you the adventuring kind and I just happen to have a bounty for someone like you.")
        print("Theres a 'Monster' that lives 'North' of here and has ben tarizing this community for too long.")
        print("So I ask you", char.name, ". Would you help us?")
        while True:
            a = input("What should you do: ")

            if a.lower() == "y" or a.lower() == "yes":
                print("That excelent!  I knew you would say that the moment I layed eyes on you.")
                input("Now you might get lost on the way so here something from me")
                bag.bag.append("map")
                input("The Mayer has givin you a map")
                input("Now if there anything more you need just ask away.")
                townHallFirst = False
                break
            elif a.lower() == "n" or a.lower() == "no":
                print("Oh I see, I was wrong about you. Well", char.name, ".")
                input("I recommend that you leave this town before it too late.")
                game_over.rejectJob(char)
            else:
                print("I dont undersatnd?  Will you help us or not?")
    else:
        print("Welcome back", char.name, ". Did you need something?")
    while True:
        print("1.) 'Were' is this monster 'location' again.\n2.) 'Ask' about the monster.\n3.) Return to the town.")
        a = input("What should you do: ")
        if bag.threeActions(a, False) == True:
            continue
        if a == "1" or a.lower() == "were" or a.lower() == "location":
            print("Its North from town up in the Mountain.\nIt should be on your map.")
            input("I would take a look at it when you reach the 'crossroads'.")
        elif a == "2" or a.lower() == "monster" or a.lower() == "ask":
            print("I personally dont know what kind of monster it is, so you should ask around town")
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            town.welcomeToTown(char, False)
        else:
            bag.invalid()
# General Store Fucntion
def generalStore(char):
    global generalStoreFirst, generalSupp

    if generalStoreFirst == True:
        print("Inside the", char.name,
              "notices vary little items in this store.\nThis store must have had better days.")
        input("A large man stood behind a table with mutton chops and his bottom lip pucker out.")

        if char.name == "Theif":
            print("Hello....", char.name, "?")
            input("Well as you can see I have nothing valuable here so why don't you 'leave'; Now.")
            generalStoreFirst = False
        else:
            print("Hello", char.name, "and welcome.")
            input("If theres anything you like just ask.")

    else:
        if char.name == "Theif":
            print("Why did you back", char.name, ".")
            input("I told you to 'leave' my store.")
        else:
            print("Welcome back", char.name, "do you still need something?")

    while True:
        print("1.) Buy Supplies.\n2.) Ask about the monster.\n3.) Return to the town.")
        a = input("What should you do: ")
        if bag.threeActions(a, False) == True:
            continue
        if a == "1" or a.lower() == "buy" or a.lower() == "supplies" or a.lower == "buy supplies" or a.lower == "buysupplies":
            if char.name == "Theif":
                input("IM NOT DOING BUSINESS WITH THE LIKES OF YOU!")
            elif char.name == "Mage":
                print("I dont think what i have would benefit a", char.name, ".")
                input("I would try the Magic Shop.")
            elif char.name == "Paladin":
                print("I dont think what i have would benefit a", char.name, ".")
                input("I would try the Church.")
            elif generalSupp == True:
                print("I dont have much to sell to you", char.name,
                      ".\nBut with that thing running around business will never pick up.")
                input("So here some potions to help out.")
                for i in range(3):
                    bag.bag.append("potion")
                generalSupp = False
                town.gotItems = True
                input("You were givin 3 potions.")
            else:
                input("Im afriend I dont have anything else that I can give you.")
        elif a == "2" or a.lower() == "ask" or a.lower() == "monster":
            if char.name == "Theif":
                print("Why yould I ever tell you anything", char.name, ".")
                input("PISS OFF!")
            else:
                print("I never see the 'Monster' myself,\nbut I think the Inn Keep might know.")
                input("I go check with her.")
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            town.welcomeToTown(char, False)
        else:
            bag.invalid()
# Magic Shop Function
def magicShop(char):
    global magicShopFirst, magicSupp

    if magicShopFirst == True:
        print("The", char.name, "was surrouned by a clutter of books, scrolls and viles fille with chemicals and magic.")
        input("The old own sat on a stool old and decrypted")
        if char.name == "Theif":
            print("Hello....", char.name, "!")
            input("I have no gold in my shop so 'leave' before you fouce my magic.")
            magicShopFirst = False
        else:
            print("Hello", char.name, ",")
            input("and welcome to my shop of magics.")

    else:
        if char.name == "Theif":
            print("Did my warnning not get thoguht you head", char.name, ".")
            input("'Leave' now or else.")
        else:
            print(char.name, "your back.")
            input("Do you still require my assistance?")

    while True:
        print("1.) Buy Supplies.\n2.) Ask about the monster.\n3.) Return to the town.")
        a = input("What should you do: ")
        if a == "1" or a.lower() == "buy" or a.lower() == "supplies" or a.lower == "buy supplies" or a.lower == "buysupplies":
            if bag.threeActions(a, False) == True:
                continue
            if char.name == "Theif":
                input("IM NEVER DO BUSINESS WITH SOMEONE IN THAT PROFESSION!")
            elif char.name == "Warrior" or char.name == "Archer":
                print("My magical inventory is too much for you", char.name, ".")
                input("The General Store would have something more to you liking.")
            elif char.name == "Paladin":
                print("I would think a", char.name,
                      "wouldn't benifit from the arcan arts.")
                input("I would ask the Church for supplies.")
            elif magicSupp == True:
                print("So your in need of my stock", char.name,
                      ".\nWell I think I can give you a few items.")
                input("These elixer would do nicely.")
                for i in range(3):
                    bag.bag.append("elixer of arcan")
                magicSupp = False
                town.gotItems = True
                input("You were givin 3 Elixer of Arcan.")
            else:
                input("Im afriend I have nothign else to offer.")
        elif a == "2" or a.lower() == "ask" or a.lower() == "monster":
            if char == "Theif":
                print("Why yould I ever tell you anything", char.name, ".")
                input("'LEAVE' MY SHOP AT ONCE!")
            else:
                print("At my age I bearly ever 'leave' my shop,\nI heard Inn Keep saw what it looks like.")
                input("I would ask her.")
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            town.welcomeToTown(char, False)
        else:
            bag.invalid()
# Church Fucntion
def church(char):
    global churchFirst, churchSupp
    if churchFirst == True:
        print("The interior of the church was large with row of pews,\nbut only a few people were there, including the priest.")
        print("The priest was a avrage sinny man, with hair only on his side as his top was compltely bare")
        print("The priest then notice the", char.name, ", and beckon thee over")
        input("Welcome to God's home, how can I help you?")
        churchFirst = False
    else:
        print("The prist notice the", char.name, "return.")
        input("What bring you back my chiled.")

    while True:
        print("1.) Buy Supplies.\n2.) Ask about the monster.\n3.) Return to the town.")
        a = input("what should you do: ")
        if a == "1" or a.lower() == "buy" or a.lower() == "supplies" or a.lower() == "buy supplies" or a.lower() == "buysupplies":
            if bag.threeActions(a, False) == True:
                continue
            if char.name == "Paladin":
                if churchSupp == True:
                    print("A", char.name, "of the church. Yes this is what I prayed for.")
                    input("Here thes holy symbles will help you vanquish this evil from our town.")
                    for i in range(3):
                        bag.bag.append("symbol of kings")
                        churchSupp = False
                        town.gotItems = True
                    input("You were givin 3 Symbol of Kings.")
                else:
                    print("Im afraid that all I have to give")
                    input("All I can do is pray for you safty.")
            else:
                print("I'll I can offer you", char.name, "is a prayer.")
                if char.name == "Warrior":
                    input("That you weapon strikes first and hard.")
                elif char.name == "Theif":
                    input("That you repent your sins of your past deeds.")
                elif char.name == "Mage":
                    input("That you repent for choices the arcan over God.")
                elif char.name == "Archer":
                    input("That you arrow strikes fast and true.")
        elif a == "2" or a.lower() == "ask" or a.lower() == "monster":
            print("Its a DEMON I tell you", char.name,
                  ".\nA DEMON who will destory this town and its inhabitants.")
            input("Will you be the Hero that this town needs?")
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            town.welcomeToTown(char, False)
        else:
            bag.invalid()
# Inn Fucntion
def inn(char):
    global innFirst
    if innFirst == True:
        print("The Inn was not as busy as most Inns should be.\nThe only people that the",
              char.name, "could see is\n the Inn Keeper and a Man in the Corner.")
        input("The Inn keep is a tall but lengthy women,\nwho notice you the moment you walked in.\nThe Man in the Corner couldn't bother to give you a glance.")
        innFirst = False
    else:
        print("The", char.name, "return to the Inn")
        input("The Inn keeper notice you.")

    while True:
        print("1.) Talk to the 'Inn Keeper'\n2.) Talk to the 'Man' in a Shadowy 'Corner'")
        a = input("Who should you talk to first: ")
        if a == "1" or a.lower() == "keeper" or a.lower() == "inn keeper" or a.lower() == "innkeeper":
            innKeeper(char)
        elif a == "2" or a.lower() == "man" or a.lower() == "corner":
            stranger(char)
        else:
            bag.invalid()
# Inkeeper Fucntion
def innKeeper(char):
    global innRumor
    while True:
        print("What do you need", char.name, ".")
        print("1.) Buy Supplies.\n2.) Ask about the monster.\n3.) Return to the town.")
        a = input("What do you want to ask: ")
        if a == "1" or a.lower() == "buy" or a.lower() == "supplies" or a.lower == "buy supplies" or a.lower == "buysupplies":
            if bag.threeActions(a, False) == True:
                continue
            print("Do I look like a Merchant to you", char.name, "?")
            if char.name == "Theif":
                print("In fact no one in this town would ever does business with a", char.name, ".")
                input("You'll have to do business in another town.")
            elif char.name == "Mage":
                print("Theres a magic shop",char.name,",")
                input(" why dont you try there",char.name,".")
            elif char.name == "Paladin":
                print("Theres a church that would help",char.name,",")
                input("go to them.")
            else:
                print("Theres a store literally called the General Store",char.name,",") 
                input("go there.")
        elif a == "2" or a.lower() == "ask" or a.lower() == "monster":
            if innRumor == True:
                print("Ya I never seen the 'monster'.\nBut the 'Huntsman' did told me he saw it while out\nhe also said I should leave while I can,\nmight have to at this point.")
                input("Hes not here right now,\nhe out in the 'Lost Forest'.\nJust head North to the 'Cross Roads' then go West.")
                innRumor = False
            else:
                input("I already told you, the 'Huntsman' is in the 'Lost Forest',\nGo North to the 'Cross Roads' then go West.\nDont you have a Map?")
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            town.welcomeToTown(char, False)
        else:
            bag.invalid()
# Stranger Fucntion
def stranger(char):
    while True:
        global theifSupp, theifInfo
        print("You walked up to the Stranger and he looked into your",char.name," eyes like icey daggers.")
        print("1.) Buy Supplies.\n2.) Ask about the monster.\n3.) Return to the town.")
        a = input("What do you want to ask: ")
        if a == "1" or a.lower() == "buy" or a.lower() == "supplies" or a.lower == "buy supplies" or a.lower == "buysupplies":
            if bag.threeActions(a, False) == True:
                continue
            if char == "Theif":
                if theifSupp == True:
                    print("Well well well, a", char.name,"whos a fellow guild member.\nIf you looken to fence here, your out of luck.")
                    print("Im as broke as everyone else in this town.\nBut if your in the bussness of killing then problem then im your man.")
                    input("Here are a few things compliments from the guild, free of charge.\nJust dont come back till its dead")
                    bag.bag.append("lock pick")
                    bag.bag.append("posion")
                    theifSupp = False
                    town.gotItems = True
                    input("You were givin Lock Pick and Posion.")
                else:
                    input("You better had done that job.\nElse why you bothering me?")
            else:
                print("Do i look like a Merchant", char.name, "?")
                input("Now piss off you dunce.")
        elif a == "2" or a.lower() == "ask" or a.lower() == "monster":
            if char == "Theif":
                if theifInfo == True:
                    print("Well I can tell you everyone in this town dont know a damn thing about it.")
                    print("Its a 'Demon Lord' and it been cutting into guild business.")
                    print("Now you never head it from me but\nin the 'Marsh Lands', east of the 'Cross Roads',\nis a large 'Tree Stump' and under it is a chest.")
                    input("Open it up and there should be something that should kill it.\nNow get that son of a bitch.")
                else:
                    print("What did you forget or somthing? You soft in the head?")
                    print("Its a Demon Lord, go to the 'Marsh Land', find the 'Tree Stump', get the weapon and kill it.")
                    input("Got it?")
                theifInfo = False
            else:
                print("Do I look like I'm in the mood to talk to a", char.name, "?")
                input("Now bugger off.")
        elif a == "3" or a.lower() == "exit" or a.lower() == "leave":
            town.welcomeToTown(char, False)
        else:
            bag.invalid()
