# Instruction screens before first frame.
# magic spells released at certain levels
# Multiple monsters
# magic cost gold.
# Map
# Monster
# Player
# # SpellBook
## ESCAPE FROM PHILADELPHIA .PY #################################
##################################################################
from random import randrange, choice
from map import Map
from monster import Monster


MAP_SIZE = 24
LIVES = [4]
monster_modes = ['ROAM', 'FIGHT']
this_monster = [0]
level = [1]

def get_level():
    return level[0]

def get_lives_func():
    return LIVES[0]

def generate_monster():
    player.level += 1
    level[0] += 1
    monsters.append(MonSteR(level[0]))

##################################################################

print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################## WELCOME TO #################### ")
print("################################################## ")
print("##########    PRINT SCREEN ADVENTURE    ########## ")
print("################################################## ")
print("### MOVE WITH ARROW KEYS OR NUMBER PAD + ENTER ### ")
print("################################################## ")
print("##### ATTACK WITH ENTER WHEN NEXT TO MONSTER ##### ")
print("################################################## ")
print("########## HEAL WITH \"h [number]\" + ENTER ######## ")
print("################################################## ")
print(" LEARN TO CAST SPELLS WITH \"cast [spell]\" + ENTER  ")
print("################################################## ")
print("#### SPELLS WILL BE REVEALED AS YOU LEVEL UP ##### ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")


class MonSteR(Monster):
# class MonSteR:
    def __init__(self, lvl ):
        Monster.__init__(self)
        self.mode = monster_modes[0]
        self.level = lvl
        self.m_typ = self.m_type()
        self.position = [randrange(2, 20), randrange(2, 20)]
        self.type = self.m_typ[0]
        self.avatar = self.m_typ[1]
        self.biom = self.m_typ[2]
        self.health = 100 * lvl
        self.inventory= [
                        {'type': 'weapon',
                          'name': self.w_name(),
                          'damage': 5 * self.level + 5},
                        {'type': 'shield',
                         'name': 'Shield',
                         'block': 5}]

    def m_type(self):
        return [
            (self.named(), " §", ".,• º∞*.  xXX"),
            (self.named(), " £", ".,•º ∞#*  xXX"),
            (self.named(), " §", ".,•º ∞*:  xXX"),
            (self.named(), " π", " ,º ∞* .;  xXX"),
            (self.named(), " £", " .,*;  xXX"),
            (self.named(), " ¥", ". •*  xXX"),
            (self.named(), " π", " .,•º∞*;#  xXX"),
            (self.named(), " ∫", ".,• º∞*;  xXX"),
            (self.named(), " £", ".,•º∞ *:  xXX"),
            (self.named(), " ƒ", " .,•º∞*:  xXX"),
            (self.named(), " §", ".,•º∞*: .  xXX"),

            # ('Lizard Man', " §", ".,• º∞*.  xXX"),
            # ('Dragon Breath', " £", ".,•º ∞#*  xXX"),
            # ('Kraken', " §", ".,•º ∞*:  xXX"),
            # ('Mage', " π", " ,º ∞* .;  xXX"),
            # ('Sith Lord', " £", " .,*;  xXX"),
            # ('Skeleton', " ¥", ". •*  xXX"),
            # ('Wizard', " π", " .,•º∞*;#  xXX"),
            # ('Lock Ness', " ∫", ".,• º∞*;  xXX"),
            # ('T-Rex', " £", ".,•º∞ *:  xXX"),
            # ("C'Thulu", " ƒ", " .,•º∞*:  xXX"),
            # ('Hydra', " §", ".,•º∞*: .  xXX")
        ][randrange(25) % 10]

    def w_name(self):
        return [
            'Club',
            'Axe',
            'Bite',
            'Tenticle',
            'Sword',
            'Lance',
            'Spike',
            'Hatchet',
            'Chainsaw'
        ][randrange(23) % 9]

    def named(self):
        adjectives = choice(['aggravating', 'annoying', 'distressing', 'disturbing', 'inconvenient', 'arduous',
                    'bothersome', 'troublesome', 'irritating', 'troublesome', 'vexing', 'exasperating', 'rebarbative incommodious',
                    'remote', 'vexatious', 'ambitious', 'demanding', 'difficile', 'exacting',
                    'wearisome', 'formidable', 'galling', 'onerous', 'operose', 'painful', 'problematic',
                    'prohibitive', 'rigid', 'severe', 'strenuous', 'titanic', 'toilsome', 'tough', 'trying', 'unyielding',
                    'burdensome', 'challenging', 'crucial', 'gargantuan', 'heavy', 'herculean', 'immense', 'irritating',
                    'labored', 'laborious'])

        place_names = choice(['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',
                    'Manayunk Railroad Yard','Skidoo Water Park Palace', 'Dunks Ferry Playground', 'Pigeons\' Gauntlet',
                    'the Inauspicious Tower of Dread at Mario Lanza Boulevard', 'the Dungeon at Dicks Ave.',
                    'the Reading Terminal Market Book Club', 'the Stronghold of Doom at Longwood Gardens',
                    'the cave under the Philadelphia Zoo', 'the dreaded Eastern State Penitentiary',
                    'the depressing, perenial dissapointment known as the Philadelphia Eagles'])

        monsterr = choice(['Rabbit', 'Troll', 'Dragon', 'Carniverous Camel', 'Loner Llama', 'Ogre', 'Slime Mold', 'Fungal Beast',
                        'Vampire', 'Dampyr', 'malformed non-specific animal', 'Shark Rocket', 'Tengu', 'Shadow Liger', 'Dragon', 'Gaslich',
                        'Hollowlich', 'Embermask', 'Bowelwraith', 'Clammy-hand Creeper', 'Creepy Cuddler', 'Mutant Tortoises of Terror',
                        'Gregarious Geek', 'Lurking Llamas', 'Horrible Screaker Witch', 'Weeping Wonderboy', 'Boston Terrier of Terror',
                        'Courier of Danger',
                        'Mutant Mummer Zombie', 'Spasm Zombie', 'Scourge', 'Wolf-man Warg', 'Water Buffalo', 'Wham-a-Whama Rock Troll',
                        'Woodland Spirit', 'Wraith', 'Wyvern', 'Murder of Crows', 'Lion-Eagle Hybrid', 'Apiarian Phantom'])
        of = choice(['of', 'from'])
        print('The {} {} {} {}'.format(adjectives, monsterr, of, place_names))
        return 'The {} {} {} {}'.format(adjectives, monsterr, of, place_names)

class Player:
    def __init__(self, health=100, gold=5, name='Zork', lvl=1, init_position=[12, 12]):
        self.position = init_position
        # self.position = [10, 1024]
        self.name = name
        self.health = health     #100
        self.gold = gold         #5
        self.inventory = self.equip()
        self.level = lvl
        self.avatar = " †"
        self.trail = "  "

    def equip(self):
        return [{'type': 'weapon', 'name': 'Axe', 'damage': 10}, {'type': 'shield', 'name': 'Shield', 'block': 5}]

    def re_equip(self):
        self.inventory = [self.new_weapon(), {'type': 'shield', 'name': 'Shield', 'block': 5}]

        # WEAPON DICTIONARY
    def new_weapon(self):
        # AQUIRE LEVEL , OR IS LEVEL A GLOBAL VARIABLE?
        return [
            {'type': 'weapon', 'name': 'Sword', 'damage': 7 * self.level},
            {'type': 'weapon', 'name': 'Spear', 'damage': 6 * self.level},
            {'type': 'weapon', 'name': 'Hammer', 'damage': 6 * self.level},
            {'type': 'weapon', 'name': 'Lance', 'damage': 8 * self.level},
            {'type': 'weapon', 'name': 'Axe', 'damage': 6 * self.level},
            {'type': 'weapon', 'name': 'Flail', 'damage': 7 * self.level},
            {'type': 'weapon', 'name': 'Spike', 'damage': 7 * self.level},
            {'type': 'weapon', 'name': 'Light Saber', 'damage': 8 * self.level},
            {'type': 'weapon', 'name': 'Reaper', 'damage': 9 * self.level}
        ][(randrange(25) ) % 9]

# player = {'name': 'ZORK', 'inventory': inventory, 'health': health, 'gold': gold}
# player['inventory'][0] = new_weapon(level[0])
##################################################################

def check_proximity(arg=2):

    for m in range(len(monsters)):
        if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(
                    monsters[m].position[1] - map.get_index_from_bit(player.position[1])):
            this_monster[0] = m
            return True
    return False


def check_death(arg):
    return arg < 0

def game_over(win):
    if win:
        map.head[0] = 4
        m0 = monsters[this_monster[0]].position[0]
        m1 = monsters[this_monster[0]].position[1]
        new_row = map.maps[map.current_map[0]][map.current_map[1]][m0][:(m1 - 1) * 2]
        new_row += ' x'
        new_row += map.maps[map.current_map[0]][map.current_map[1]][m0][m1 * 2:]
        # map.message_key[1] = 'killedit'
        map.maps[map.current_map[0]][map.current_map[1]][m0] = new_row

        # determine which monster
        z = monsters.pop(this_monster[0])
        map.message_key[1] = 'killedit'
        generate_monster()
    else:
        LIVES[0] -= 1
        if LIVES[0] > 0:
            map.reincarnate(player, monsters)
        else:
            map.head[0] = 3
            map.header(player)
            quit()

def monster_attack(m):
    v = monsters[m].inventory[0]['damage'] - player.inventory[1]['block']
    player.health -= v
    if check_death(player.health):
        game_over(False)
    map.message_key[2] = 'dmg ' + str(monsters[m].inventory[0]['damage'])

########################################################################################################################

def player_attack(arg):
    print(arg)
    if arg == 'kill':
        monsters[this_monster[0]].health = monsters[this_monster[0]].health - (player.inventory[0]['damage'] * 10)
        map.head[0] = 2
    elif arg.lower() == 'zero':
        monsters[this_monster[0]].health = 0
        map.head[0] = 2
    elif arg.lower() == 'zork':
        monsters[this_monster[0]].health = monsters[this_monster[0]].health - (player.inventory[0]['damage'] * 90)
        map.head[0] = 2
    else:
        monsters[this_monster[0]].health -= int(player.inventory[0]['damage'] +
                                                (player.gold * .01))  - monsters[this_monster[0]].inventory[1]['block']
    if check_death(monsters[this_monster[0]].health):
        game_over(True)
    map.monster_go(player, monsters)
    map.mapit(player, monsters)

########################################################################
######################  SPELL BOOK  ####################################
########################################################################
def heal_self(arg='9'):
    print(arg)
    try:
        player.gold = player.gold - int(arg)
        player.health = player.health + int(arg)
    except:
        map.monster_go(player, monsters)

def cast_spell(spell=''):
    if spell[:5] == 'black' and player.gold > 60:
        player.gold -= 60
        if check_proximity(4):
            player_attack('kill')

    elif spell[:4] == 'zero' and player.gold > 100:
        player.gold -= 100
        if check_proximity(1):
            player_attack(spell)

    elif spell[:4] == 'five' and player.gold > 50:
        player.gold -= 50
        if check_proximity(5):
            player_attack(spell)

    elif spell[:6] == 'orange' and player.gold > 10:
        player.gold -= 10
        if check_proximity(9):
            player_attack(spell)

    elif spell[:5] == 'death' and player.gold > 100:
        player.gold -= 100
        if check_proximity(20):
            player_attack('kill')

    elif spell == '' and player.gold > 30:
        player.gold -= 30
        if check_proximity(3):
            player_attack(spell)

    elif spell == 'live' and player.gold > 1000:
        player.gold -= 1000
        LIVES[0] += 1
        # player_attack()

    else:
        if check_proximity():
            player_attack(spell)

########################################################################
###################### //SPELL BOOK  ###################################
########################################################################

monsters = [MonSteR(1), MonSteR(1), MonSteR(1)]
player = Player()

def get_monsters_fn():
    return monsters

map = Map(player, monsters, monster_attack, get_level, get_lives_func, get_monsters_fn)
map.mapit(player, monsters)

while True:
    command = input("Type Command: ( n s e w a(t)tack cast heal x:exit )\n>>> ")
    if command[:2] == 'at' or 't' == command[:1] or command[:1] == 'w' or ' ' == command[:1] or '' == command[:1]:
        if check_proximity():
            player_attack(command[command.find(" ") + 1:])
        else:
            map.move(0, player, monsters)

    elif command[:4] == 'cast' or 'c' == command[:1]:
        cast_spell(command[command.find(' ')+1:])
        map.head[0] = 1
        map.mapit( player, monsters)

    elif command[:4] == 'heal' or 'h' == command[:1]:
        if command.find(' ') > -1:
            heal_self(command[command.find(' '):])
        else:
            heal_self()
        map.head[0] = 0
        map.mapit( player, monsters)

    else:
        for i in range(len(command)):
            if command[i] == 'x':
                if input('      Are you sure you want to quit? (c) ') == 'c':
                    quit()
            elif command[i] == 'n' or '2' == command[i] or 'A' == command[i]:
                map.move(2, player, monsters)
            elif command[i] == 's' or '8' == command[i] or 'B' == command[i]:
                map.move(8, player, monsters)
            elif command[i] == 'e' or '6' == command[i] or 'C' == command[i]:
                map.move(6, player, monsters)
            elif command[i] == 'q' or '4' == command[i] or 'D' == command[i]:
                map.move(4, player, monsters)
            elif command[i] == '1':
                map.move(1, player, monsters)
            elif command[i] == '3':
                map.move(3, player, monsters)
            elif command[i] == '7' or 'a' == command[i]:
                map.move(7, player, monsters)
            elif command[i] == '9' or 'd' == command[i]:
                map.move(9, player, monsters)

