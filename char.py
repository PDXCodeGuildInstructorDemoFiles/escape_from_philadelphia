from char_class import CharacterAttributes
from inventory import Inventory


class Character:
    def __init__(self, name):
        self.name = name
        self.cls = self.choose_class()
        self.inv = self.create_inv()
        self.level = 1
        self.avatar = ' {} '
        self.location = (0, 1)

    def choose_class(self):
        print('''Press 1 for Nuke Elf, 2 for Human, 3 for Zombie, 4 for Lemur, 5 for Gorilla, 6 for Cyborg, 
                 7 for Technovore, 8 for Mid-night Elf or 9 for Bear''')
        d = {1: 'nuke_elf',
             2: 'The Who Man',
             3: 'Charasaurus Rex: First Bite',
             4: 'Huey the Furious Furry Ruffed Lemur of Acrimonious Vengeance',
             5: 'Motuba the Gorilla Guardian of the Broad Street Subway Band',
             6: 'Cyborg Cyndi: Iron Woman',
             7: 'Electro Slug @ South Street',
             8: 'The Marauding Midnight Elf',
             9: 'Warrior Samurai Bear'}
        q = int(input('What class do you choose? '))
        return CharacterAttributes(d[q])

    def create_inv(self):
        return Inventory('player bag', 50)

    def __str__(self):
        return 'HP: {}, Total Armor: {}, weapon: {}, equipped armor: {}'.format(self.cls.hp, self.cls.armor, self.inv.weapon, self.inv.armor)

if __name__ == '__main__':
    q = input('Hello what is your name? ')
    player = Character(q)

    # print(player.name)


    def include_name(plr):
        if plr.cls.name == 'Charasaurus Rex: First Bite' \
                            or plr.cls.name == 'Huey the Furious Furry Ruffed Lemur of Acrimonious Vengeance' \
                            or plr.cls.name == 'Motuba the Gorilla Guardian of the Broad Street Subway Band'\
                            or plr.cls.name == 'Cyborg Cyndi: Iron Woman':
            print('Excellent {}!  You are now {}! Let us begin!'.format(plr.name, plr.cls.name))
        else:
            print('Excellent!  You are now {}, {}!  Let us begin!'.format(plr.name, plr.cls.name))

    include_name(player)


    def generate_character():
        pass
