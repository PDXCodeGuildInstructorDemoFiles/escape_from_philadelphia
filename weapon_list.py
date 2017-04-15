'''
Added luck which allows us to set a percentage to the weapon drops based on rarity. Added armor
and weapons. Will try to make a master dictionary which will allow us to have a key for each rarity. 
'''

import math
import random

basic_armor = ['Construction Chaps', 'Motorcycle Helmet', 'Leather Gloves', 'Welding Helmet']

common_armor = ['Kevlar Vest', 'Iron Chest Plate', 'Steel Toe Boots']

rare_armor = ['Bullet Proof Suit', 'Viking Helmet', 'Steel Chest Plate']

epic_armor = ['Titanium Cuffs', 'Mech Body Armor']

legendary_armor = ['Plasma shield', 'Obsidian Chest Plate']


basic_weapons = ['Baseball Bat', 'Crow Bar', 'Hunting Knife', 'Pepper Spray']

common_weapons = ['.22 Pistol', 'Pump Shotgun', 'Crossbow']

rare_weapons = ['AR-15', 'Elephant Gun', 'Hunting Rifle']

epic_weapons = ['Flamethrower', 'Rocket Launcher', 'Grenade Launcher']

legendary_weapons = ['Gatling Gun', 'Sword of Doom', 'Laser Rifle', 'Mech Cannon', 'MOAG (Mother of All Guns']


class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect, self.weight)

'''
Functions for creating our weapons
'''

def create_basic_weapon():
    return Items(random.choice(basic_weapons), 'basic weapon', random.randrange(1, 10) * lvl, random.randrange(1, 8))

def create_common_weapon():
    return Items(random.choice(common_weapons), 'common weapon', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))

def create_rare_weapon():
    return Items(random.choice(rare_weapons), 'rare weapon', random.randrange(3, 10) * (lvl * 2.5), random.randrange(1, 6))

def create_epic_weapon():
    return Items(random.choice(epic_weapons), 'epic weapon', random.randrange(4, 10) * (lvl * 3), random.randrange(1, 5))

def create_legendary_weapon():
    return Items(random.choice(legendary_weapons), 'legendary weapon', random.randrange(5, 10) * (lvl * 4), random.randrange(1, 4))

'''
functions for creating certain levels and rarities of armor
'''

def create_basic_armor():
    return Items(random.choice(basic_armor), 'basic armor', random.randrange(1, 8), random.randrange(1, 10))

def create_common_armor():
    return Items(random.choice(common_armor), 'common armor', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))

def create_rare_armor():
    return Items(random.choice(rare_armor), 'rare armor', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))

def create_epic_armor():
    return Items(random.choice(epic_armor), 'epic armor', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))

def create_legendary_armor():
    return Items(random.choice(legendary_armor), 'legendary armor', random.randrange(2, 10) * (lvl * 2), random.randrange(1, 7))

def create_weapon():
    luck = random.randrange(1, 101)
    if luck in range(1, 50):
        return create_basic_weapon()
    elif luck in range(50, 75):
        return create_common_weapon()
    elif luck in range(75, 85):
        return create_rare_weapon()
    elif luck in range(85, 97):
        return create_epic_weapon()
    else:
        if luck in range(97, 101):
            return create_legendary_weapon()

def create_armor():
    luck = random.randrange(1, 101)
    if luck in range(1, 50):
        return create_basic_armor()
    elif luck in range(50, 75):
        return create_common_armor()
    elif luck in range(75, 85):
        return create_rare_armor()
    elif luck in range(85, 97):
        return create_epic_armor()
    else:
        if luck in range(97, 101):
            return create_legendary_armor()

'''
First aid function creates a random number and then generates a first aid based on the random number. 
I made sure to give the random number a better chance of landing on something average, and
a very rare chance of landing on something rare
'''

def create_first_aid():
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
        return Items('nano goo', 'first aid', nano_goo_range * lvl, 0)
    elif aid_level in range(4, 8):
        return Items('greater healing potion', 'first aid', greater_healing_potion_range * lvl, 1)
    elif aid_level in range(8, 15):
        return Items('water', 'first aid', water_range * lvl, 1)
    elif aid_level in range(15, 35):
        return Items('bandages', 'first aid', bandages_range * lvl, 2)
    elif aid_level in range(35, 40):
        return Items('first aid kit', 'first aid', first_aid_kit_range * lvl, 3)
    elif aid_level in range(40, 47):
        return Items('antibiotics', 'first aid', antibiotics_range * lvl, 1)
    elif aid_level in range(47, 51):
        return Items('medical pack', 'first aid', medical_pack_range * lvl, 0)


# lvl = random.randrange(1, 10)
lvl = 1
aid1 = create_first_aid()
aid2 = create_first_aid()
aid3 = create_first_aid()
aid4 = create_first_aid()
aid5 = create_first_aid()

print(aid1)
print(aid2)
print(aid3)
print(aid4)
print(aid5)

# weapon1 = create_weapon()
# weapon2 = create_weapon()
# weapon3 = create_weapon()
# weapon4 = create_weapon()
# weapon5 = create_weapon()
# weapon6 = create_weapon()
# weapon7 = create_weapon()
# weapon8 = create_weapon()
# weapon9 = create_weapon()
# weapon10 = create_weapon()
#
# print(weapon1)
# print(weapon2)
# print(weapon3)
# print(weapon4)
# print(weapon5)
# print(weapon6)
# print(weapon7)
# print(weapon8)
# print(weapon9)
# print(weapon10)
#
# armor1 = create_armor()
# armor2 = create_armor()
# armor3 = create_armor()
# armor4 = create_armor()
# armor5 = create_armor()
# armor6 = create_armor()
# armor7 = create_armor()
# armor8 = create_armor()
# armor9 = create_armor()
# armor10 = create_armor()
#
# print(armor1)
# print(armor2)
# print(armor3)
# print(armor4)
# print(armor5)
# print(armor10)
# print(armor6)
# print(armor7)
# print(armor8)
# print(armor9)