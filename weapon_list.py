import random

basic_armor = ['Construction Chaps', 'Motorcycle Helmet', 'Leather Gloves', 'Welding Helmet']

common_armor = ['Kevlar Vest', 'Iron Chest Plate', 'Steel Toe Boots']

rare_armor = ['Bullet Proof Suit', 'Viking Helmet', 'Steel Chest Plate']

epic_armor = ['Titanium Cuffs', 'Mech Body Armor']

legendary_armor = ['Plasma shield', 'Obsidian Chest Plate']

basic_weapons = ['Baseball Bat', 'Crow Bar', 'Hunting Knife' ]

common_weapons = ['.22 Pistol', 'Pump Shotgun', '']

rare_weapons = ['AR-15', 'Elephant Gun', 'Hunting Rifle']

epic_weapons = ['Flamethrower', 'Rocket Launcher', 'Grenade Launcher']

legendary_weapons = ['Gatling Gun', 'Sword of Doom', 'Laser Rifle', 'Mech Cannon', 'MOAG (Mother of All Guns']

fa_names = ['Elixir of Life', 'Greater Healing Potion', 'Lesser Healing Potion', 'Water']

class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect, self.weight)

def create_basic_weapon():
    return Items(random.choice(basic_weapons), 'basic weapon', random.randrange(1, 10) * lvl, random.randrange(1, 5) * lvl)

def create_common_weapon():
    return Items(random.choice(common_weapons), 'common weapon', random.randrange(1, 10) * (lvl * 1.5), random.randrange(1,10) * (lvl * 1.5))

def create_rare_weapon():
    return Items(random.choice(rare_weapons), 'rare weapon', random.randrange(1, 10) * (lvl * 2.5), random.randrange(1,10) * (lvl * 2.5))

def create_epic_weapon():
    return Items(random.choice(epic_weapons), 'epic weapon', random.randrange(1, 10) * (lvl * 5), random.randrange(1, 10) * (lvl * 5))

def create_legendary_weapon():
    return Items(random.choice(legendary_weapons), 'legendary weapon', random.randrange(1, 10) * (lvl * 8), random.randrange(1, 10) * (lvl * 8))

def create_basic_armor():
    return Items(random.choice(basic_armor), 'basic armor', random.randrange(1, 10), random.randrange(1, 50))


def create_first_aid():
    return Items(random.choice(fa_names), 'first aid', random.randrange(2, 20), random.randrange(1, 5))

lvl = 1

basic_weapon = create_basic_weapon()
common_weapon = create_common_weapon()
rare_weapon = create_rare_weapon()
epic_weapon = create_epic_weapon()
legendary_weapon = create_legendary_weapon()

print(basic_weapon)
print(common_weapon)
print(rare_weapon)
print(epic_weapon)
print(legendary_weapon)

