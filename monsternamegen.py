import random
import time


def genMonstername():
    list1 = ["Terrible", "Horrible", "Rebarbative", "Incommodious", "aggravating", "annoying", "distressing", "disturbing", "inconvenient", "irritating", "troublesome", "vexing", "exasperating", "incommodious", "remote", "tiresome", "vexatious", "giggling", "insidious","aggravating”, “annoying”, “distressing”, “disturbing”, “inconvenient”,
            "arduous”, “backbreaker”, “bothersome”, “troublesome”, , “irritating”,
            "troublesome”, “vexing”, “exasperating”, “incommodious”, “remote”, “vexatious”, “ambitious”,
            "demanding”, “difficile”, “effortful”, “exacting”, “wearisome”, “formidable”, “galling”,
            "onerous", "painful", "problem", "problematic", "prohibitive", "rigid”, “severe”,
            "stiff”, “strenuous”, “titanic”, “toilsome”, “tough”, “trying”, “unyielding”, “uphill”,
            "upstream”, “burdensome”, “challenging”, “crucial”, “gargantuan”, “heavy”,
            "herculean"", “immense”, “intricate”, “irritating”, “labored”, “laborious”]
    list2 = ["Rabbit", "Troll", "Dragon", "Camel", "Llama", "Ogre", "Slime Mold", "Fungal Beast", "Vampire", "Dampyr", "Malformed animal", "Shark Rocket", "Tengu", "Zombie", "Shadow", "Dragon", "Gaslich", "Hollowlich", "Embermask", "Bowelwraith", "Biters", "Cold Bodies",    CREEPER    DEAD ONES    FLOATERS    GEEK    LAMEBRAINS    LURKERS    Screaker    Weeper    Tearer    Courier    Crowd Zombie    Gagger    Blaster    Licker    Spasm Zombie    Scourge    wolf Warg    Water Hag    Wham-a-Wham    Woodland Spirit    Wraith    Wyvern    foglet    Tangalore     "Therazane","Apiarian Phantom""]
    list3 = ['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',
               'Manayunk Railroad Yard','Skidoo Water Park Palace', 'Dunks Ferry Playground', 'Pigeons\' GauntleCREEPER    DEAD ONES    FLOATERS    GEEK    LAMEBRAINS    LURKERS    Screaker    Weeper    Tearer    Courier    Crowd Zombie    Gagger    Blaster    Licker    Spasm Zombie    Scourge    wolf Warg    Water Hag    Wham-a-Wham    Woodland Spirit    Wraith    Wyvern    foglet    Tangalore     "Therazane","Apiarian Phantom""]
    list3 = ['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',t',
               'the Inauspicious Tower of Dread at Mario Lanza Boulevard', 'the Dungeon at Dicks Ave.',
               'the Reading Terminal Market Book Club', 'the Stronghold of Doom at Longwood Gardens',
               'the cave under the Philadelphia Zoo', 'the dreaded Eastern State Penitentiary',
               'the depressing, perennial disappointment known as the Philadelphia Eagles']

    sel1 = random.randint(0, len(list1) - 1)
    sel2 = random.randint(0, len(list2) - 1)
    sel3 = random.randint(0, len(list3) - 1)
    print ("The " + list1[sel1] + " " + list2[sel2] + " " + "of " + list3[sel3])


while True:
    genMonstername()
