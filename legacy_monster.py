from random import randrange


class Monster:
    def __init__(self, lvl ):
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
            ('Lizard Man', " §", ".,• º∞* xXX"),
            ('Dragon Breath', " £", ".,•º ∞* xXX"),
            ('Kraken', " §", ".,•º ∞*:"),
            ('Mage', " π", " ,º ∞* .;"),
            ('Sith Lord', " £", " .,*;"),
            ('Skeleton', " ¥", ". •* xXX"),
            ('Wizard', " π", " .,•º∞*;"),
            ('Lock Ness', " ∫", ".,• º∞*;"),
            ('T-Rex', " £", ".,•º∞*:"),
            ("C'Thulu", " ƒ", " .,•º∞*:"),
            ('Hydra', " §", ".,•º∞*: .")
        ][randrange(25)  % 10]

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
        ][randrange(23)  % 9]


