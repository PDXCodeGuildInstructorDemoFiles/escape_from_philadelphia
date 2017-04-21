import math
import random
from items import Items

master_list = {
    'basic_armor': ['Cloth Armor', 'Grandmas Knitted Armor', 'Animal Hide Armor', 'Scuba Diving Suit', 'Weak Ass Armor'],
    'common_armor': ['Kevlar Armor', 'Motorcycle Armor', 'Football Pads', 'Reinforced Armor'],
    'rare_armor': ['Iron Armor', 'Viking Armor', 'Warrior Armor', 'Heavy Ass Armor'],
    'epic_armor': ['Steel Armor', 'Titanium Armor', 'Force Reduction Armor', 'Wonderwomans Cape'],
    'legendary_armor': ['Plasma shield Armor', 'Obsidian Armor', 'Mech Armor', 'Supermans Cape'],
    'basic_weapon': ['Baseball Bat', 'Crow Bar', 'Hunting Knife', 'Pepper Spray', 'Old Taser', 'BB Gun', 'Machete'],
    'common_weapon': ['.22 Pistol', 'Pump Shotgun', 'Crossbow', 'Samurai Sword', 'Throwing Stars', 'Molotov Cocktail'],
    'rare_weapon': ['AR-15', 'Elephant Gun', 'Hunting Rifle', 'Double Barrel Shotgun', '.44 Mag Revolver', 'Old Sniper Rifle'],
    'epic_weapon': ['Flamethrower', 'Rocket Launcher', 'Grenade Launcher', 'Custom Pistols', 'Radiated Poison Knife'],
    'legendary_weapon': ['Gatling Gun', 'Sword of Doom', 'Laser Rifle', 'Mech Cannon', 'MOAG (Mother of All Guns', 'Light Saber']}


def create_basic(type, lvl):
    return Items(random.choice(master_list['basic_' + str(type)]), 'basic ' + str(type), random.randrange(1, 10) * lvl,
                 random.randrange(1, 4), random.randrange(5, 16) * lvl)

def create_common(type, lvl):
    return Items(random.choice(master_list['common_' + str(type)]), 'common ' + str(type),
                 random.randrange(3, 7) * (lvl * 1.5), random.randrange(1, 7), random.randrange(15, 26) * lvl)

def create_rare(type, lvl):
    return Items(random.choice(master_list['rare_' + str(type)]), 'rare ' + str(type),
                 random.randrange(6, 10) * (lvl * 2), random.randrange(1, 6), random.randrange(25, 36) * lvl)

def create_epic(type, lvl):
    return Items(random.choice(master_list['epic_' + str(type)]), 'epic ' + str(type),
                 random.randrange(9, 13) * (lvl * 3), random.randrange(1, 5), random.randrange(35, 46) * lvl)

def create_legendary(type, lvl):
    return Items(random.choice(master_list['legendary_' + str(type)]), 'legendary ' + str(type),
                 random.randrange(15, 20) * (lvl * 5), random.randrange(1, 3), random.randrange(100, 200) * lvl)


def create_weapon(lvl):
    luck = random.randrange(1, 101)
    if luck in range(1, 50):
        return create_basic('weapon', lvl)
    elif luck in range(50, 75):
        return create_common('weapon', lvl)
    elif luck in range(75, 85):
        return create_rare('weapon', lvl)
    elif luck in range(85, 98):
        return create_epic('weapon', lvl)
    elif luck in range(98, 101):
        return create_legendary('weapon', lvl)

# CODE TESTING
# weapon1 = create_weapon()
# print(weapon1)

def create_armor(lvl):
    luck = random.randrange(1, 101)
    if luck in range(1, 50):
        return create_basic('armor', lvl)
    elif luck in range(50, 75):
        return create_common('armor', lvl)
    elif luck in range(75, 85):
        return create_rare('armor', lvl)
    elif luck in range(85, 97):
        return create_epic('armor', lvl)
    elif luck in range(97, 101):
        return create_legendary('armor', lvl)


'''
First aid function creates a random number and then generates a first aid based on the random number.
I made sure to give the random number a better chance of landing on something average, and
a very rare chance of landing on something rare
'''


def create_first_aid(lvl):
    random_number = random.triangular(1, 50, 20)
    aid_level = math.trunc(random_number)
    water_range = random.randrange(1, 5)
    bandages_range = random.randrange(5, 10)
    first_aid_kit_range = random.randrange(10, 15)
    antibiotics_range = random.randrange(15, 20)
    medical_pack_range = random.randrange(20, 25)
    greater_healing_potion_range = random.randrange(25, 30)
    nano_goo_range = random.randrange(30, 40)
    if aid_level in range(1, 4):
        return Items('nano goo', 'first aid', nano_goo_range * lvl, 0, random.randrange(20, 41))
    elif aid_level in range(4, 8):
        return Items('greater healing potion', 'first aid', greater_healing_potion_range * lvl, 1, random.randrange(15, 21))
    elif aid_level in range(8, 15):
        return Items('water', 'first aid', water_range * lvl, 1, random.randrange(1, 3))
    elif aid_level in range(15, 35):
        return Items('bandages', 'first aid', bandages_range * lvl, 2, random.randrange(2, 4))
    elif aid_level in range(35, 40):
        return Items('first aid kit', 'first aid', first_aid_kit_range * lvl, 3, random.randrange(3, 7))
    elif aid_level in range(40, 47):
        return Items('antibiotics', 'first aid', antibiotics_range * lvl, 1, random.randrange(7, 11))
    elif aid_level in range(47, 51):
        return Items('medical pack', 'first aid', medical_pack_range * lvl, 0, random.randrange(10, 16))


if __name__ == '__main__':
    lvl = random.randrange(1, 10)
    lvl = 1
    aid1 = create_first_aid(lvl)
    aid2 = create_first_aid(lvl)
    aid3 = create_first_aid(lvl)
    aid4 = create_first_aid(lvl)
    aid5 = create_first_aid(lvl)

    print(aid1)
    print(aid2)
    print(aid3)
    print(aid4)
    print(aid5)

    weapon1 = create_weapon(lvl)
    weapon2 = create_weapon(lvl)
    weapon3 = create_weapon(lvl)
    weapon4 = create_weapon(lvl)
    weapon5 = create_weapon(lvl)
    weapon6 = create_weapon(lvl)
    weapon7 = create_weapon(lvl)
    weapon8 = create_weapon(lvl)
    weapon9 = create_weapon(lvl)
    weapon10 = create_weapon(lvl)

    print(weapon1)
    print(weapon2)
    print(weapon3)
    print(weapon4)
    print(weapon5)
    print(weapon6)
    print(weapon7)
    print(weapon8)
    print(weapon9)
    print(weapon10)

    armor1 = create_armor(lvl)
    armor2 = create_armor(lvl)
    armor3 = create_armor(lvl)
    armor4 = create_armor(lvl)
    armor5 = create_armor(lvl)
    armor6 = create_armor(lvl)
    armor7 = create_armor(lvl)
    armor8 = create_armor(lvl)
    armor9 = create_armor(lvl)
    armor10 = create_armor(lvl)

    print(armor1)
    print(armor2)
    print(armor3)
    print(armor4)
    print(armor5)
    print(armor10)
    print(armor6)
    print(armor7)
    print(armor8)
    print(armor9)
