from random import randrange


class CharacterAttributes:
    def __init__(self, cn):
        self.hp = None
        self.name = None
        self.exp = None
        self.stamina = None
        self.armor = None
        self.strength = None
        self.magic = None
        self.intelligence = None
        self.set_stats(cn)

    def set_stats(self, cn):
        slug = cn.replace(' ', '_').lower()
        classes = {
            'nuke_elf': self.nuke_elf,
            'the_who_man': self.human,
            'charasaurus_rex:_first_bite': self.zombie,
            'huey_the_furious_furry_ruffed_lemur_of_acrimonious_vengeance': self.lemur,
            'motuba_the_gorilla_guardian_of_the_broad_street_subway_band': self.gorilla,
            'cyborg_cyndi:_iron_woman': self.cyborg,
            'electro_slug_@_south_street': self.technovore,
            'the_marauding_midnight_elf': self.midnight_elf,
            'warrior_samurai_bear': self.bear
        }
        classes[slug]()

    def nuke_elf(self):
        self.name = 'Nuke Elf'
        self.hp = randrange(7, 20)
        self.exp = randrange(1, 15)
        self.stamina = randrange(10, 20)
        self.armor = randrange(5, 25)
        self.strength = randrange(15, 30)
        self.magic = randrange(5, 30)
        self.intelligence = randrange(7, 15)
        # nuke_elf starts at a higher class but should have some vulnerabilities such as high viz
        # so they get hit a lot

    def human(self):
        self.name = 'The Who-Man'
        self.hp = randrange(3, 15)
        self.exp = randrange(1, 15)
        self.stamina = randrange(4, 7)
        self.armor = randrange(3, 10)
        self.strength = randrange(3, 15)
        self.magic = randrange(5, 15)
        self.intelligence = randrange(7, 15)

    def zombie(self):
        self.name = 'Charasaurus Rex: First Bite'
        self.hp = randrange(10, 30)
        self.exp = randrange(1, 7)
        self.stamina = randrange(3, 15)
        self.armor = randrange(1, 7)
        self.strength = randrange(1, 5)
        self.magic = randrange(1, 3)
        self.intelligence = randrange(1, 5)

    def lemur(self):
        self.name = 'Huey the Furious Furry Ruffed Lemur of Acrimonious Vengeance'
        self.hp = randrange(10, 27)
        self.exp = randrange(1, 15)
        self.stamina = randrange(3, 10)
        self.armor = randrange(2, 10)
        self.strength = randrange(3, 10)
        self.magic = randrange(3, 10)
        self.intelligence = randrange(3, 17)

    def gorilla(self):
        self.name = 'Motuba the Gorilla Guardian of the Broad Street Subway Band'
        self.hp = randrange(10, 27)
        self.exp = randrange(1, 15)
        self.stamina = randrange(10, 25)
        self.armor = randrange(10, 25)
        self.strength = randrange(15, 30)
        self.magic = randrange(1, 10)
        self.intelligence = randrange(3, 15)

    def cyborg(self):
        self.name = 'Cyborg Cyndi: Iron Woman'
        self.hp = randrange(15, 30)
        self.exp = randrange(1, 15)
        self.stamina = randrange(15, 25)
        self.armor = randrange(15, 25)
        self.strength = randrange(15, 30)
        self.magic = randrange(2, 15)
        self.intelligence = randrange(15, 30)

    def technovore(self):
        self.name = 'Electro-Slug @ South Street'
        self.hp = randrange(15, 30)
        self.exp = randrange(1, 15)
        self.stamina = randrange(15, 25)
        self.armor = randrange(15, 25)
        self.strength = randrange(15, 30)
        self.magic = randrange(2, 15)
        self.intelligence = randrange

    def midnight_elf(self):
        self.name = 'The Marauding Midnight Elf'
        self.hp = randrange(7, 20)
        self.exp = randrange(1, 15)
        self.stamina = randrange(10, 20)
        self.armor = randrange(5, 25)
        self.strength = randrange(15, 30)
        self.magic = randrange(10, 30)
        self.intelligence = randrange(7, 15)

    def bear(self):
        self.name = 'Warrior Samurai Bear'
        self.hp = randrange(10, 25)
        self.exp = randrange(1, 15)
        self.stamina = randrange(10, 25)
        self.armor = randrange(15, 25)
        self.strength = randrange(15, 30)
        self.magic = randrange(10, 17)
        self.intelligence = randrange(7, 25)

    def kangaroo(self):
        self.name = 'Thumperoo: Steel Fisted World Champion Kick Boxer'
        self.hp = randrange()
        self.exp = randrange()
        self.stamina = randrange()
        self. armor = randrange()
        self.strength = randrange()
        self.magic  = randrange()
        self.intelligence = randrange()

    def snake(self):
        self.name = 'Scaler the deceptive boa constrictor'
        self.hp = randrange()
        self.exp = randrange()
        self.stamina = randrange()
        self. armor = randrange()
        self.strength = randrange()
        self.magic  = randrange()
        self.intelligence = randrange()

    def rhinosorus(self):
        self.name = 'Crush Thunder the thunderous earth shacking Rhino'
        self.hp = randrange()
        self.exp = randrange()
        self.stamina = randrange()
        self. armor = randrange()
        self.strength = randrange()
        self.magic  = randrange()
        self.intelligence = randrange()


    def hawk(self):
        self.name = 'Striker Hawk'
        self.hp = randrange()
        self.exp = randrange()
        self.stamina = randrange()
        self. armor = randrange()
        self.strength = randrange()
        self.magic  = randrange()
        self.intelligence = randrange()