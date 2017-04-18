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
            'human': self.human,
            'zombie': self.zombie,
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
        self.intelligence = (7, 15)
        # nuke_elf starts at a higher class but should have some vulnerabilities such as high viz
        # so they get hit a lot

    def human(self):
        self.name = 'Who-Man'
        self.hp = randrange(3, 15)
        self.exp = randrange(1, 15)
        self.stamina = randrange(3, 7)
        self.armor = randrange(2, 10)
        self.strength = randrange(3, 15)
        self.magic = randrange(5, 15)
        self.intelligence = (7, 15)

    def zombie(self):
        self.hp = randrange(10, 30)
        self.exp = randrange(1, 7)
        self.stamina = randrange(3, 15)
        self.armor = randrange(1, 7)
        self.strength = randrange(1, 5)
        self.magic = randrange(1, 3)
        self.intelligence = (1, 5)
