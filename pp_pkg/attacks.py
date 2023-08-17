def attackOptions():
    print("1.) Charge\n2.) Shoot\n3.) Cast\n4.) Sneak")

def noProjectile(char):
    print("The",char.name,"doesn't have any projectile weapon.")
    input("So nothing happen.")

def noSpells(char):
    print("The",char.name,"doesn't know nay spells")
    input("So nothing happen.")

def necroCharge(char):
    print("The",char.name,"charges towards the Necro Manser.")
    print("The Necro Manser cast a spell but the",char.name,"was able to doge in time.")

def necroArcan(char):
    print("The power of arcan rush thought your body and you cast a massive",char.spell,"towards the 'Necor Manser'.")
    input("The 'Necro Manser' was reduce to a pile of ash.")

def necroSymbol(char):
    print("The power of God fill you to your core and you cast",char.spell,"at the 'Necro Manser'.")
    input("THe 'Necro Manser' was reduce to a pile of ash.")