from random import randrange, choice
from monsternamegen import genMonstername

#
class Monster:
    '''this is intended as a base attribute list for our monsters'''

    def __init__(self):
        """be sure to add weapons back into the function down the road.  
        add attribute position which will be a list where 0 = y & 1 = x.  
        this will be come clear later."""

        self.mode = None  # 'ROAM' also includes 'FIGHT' when one must fight - function to follow?
        self.avatar = None
        self.hp = None
        self.strength = None
        self.armor = None
        self.magic = None
        # self.m_typ = self.m_type() #touch base with Joe re: this and the succeeding attribute
        # self.biom = self.m_typ

    def __str__(self):
        return 'hp: {}, strength: {}, armor: {}, magic: {}'.format(self.hp, self.strength, self.armor, self.magic)

    def generate_monster(self, level):
        '''generates a monster based on certain ranges corresponding to a level as determined at some later time'''
        self.hp = randrange(40, 100) * level
        self.strength = randrange(60, 100)
        self.armor = int(round((self.hp * self.strength) / 200, 0))
        self.magic = randrange(40, 100)
        self.name = genMonstername()
        self.exp = randrange(1, 15)
        self.stamina = randrange(10, 20)
        self.intelligence = randrange(7, 15)
        self.avatar = ' 👹  '




    adjectives = choice(['aggravating', 'annoying', 'distressing', 'disturbing', 'inconvenient', 'arduous',
                         'bothersome', 'troublesome', 'irritating', 'troublesome', 'vexing', 'exasperating',
                         'rebarbative incommodious',
                         'remote', 'vexatious', 'ambitious', 'demanding', 'difficile', 'exacting',
                         'wearisome', 'formidable', 'galling', 'onerous', 'operose', 'painful', 'problematic',
                         'prohibitive', 'rigid', 'severe', 'strenuous', 'titanic', 'toilsome', 'tough', 'trying',
                         'unyielding',
                         'burdensome', 'challenging', 'crucial', 'gargantuan', 'heavy', 'herculean', 'immense',
                         'irritating',
                         'labored', 'laborious'])

    place_names = choice(['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',
                          'Manayunk Railroad Yard', 'Skidoo Water Park Palace', 'Dunks Ferry Playground',
                          'Pigeons\' Gauntlet',
                          'the Inauspicious Tower of Dread at Mario Lanza Boulevard', 'the Dungeon at Dicks Ave.',
                          'the Reading Terminal Market Book Club', 'the Stronghold of Doom at Longwood Gardens',
                          'the cave under the Philadelphia Zoo', 'the dreaded Eastern State Penitentiary',
                          'the depressing, perenial dissapointment known as the Philadelphia Eagles'])

    monster = choice(
        ['Rabbit', 'Troll', 'Dragon', 'Carniverous Camel', 'Loner Llama', 'Ogre', 'Slime Mold', 'Fungal Beast',
         'Vampire', 'Dampyr', 'malformed non-specific animal', 'Shark Rocket', 'Tengu', 'Shadow Liger', 'Dragon',
         'Gaslich',
         'Hollowlich', 'Embermask', 'Bowelwraith', 'Clammy-hand Creeper', 'Creepy Cuddler',
         'Mutant Tortoises of Terror',
         'Gregarious Geek', 'Lurking Llamas', 'Horrible Screaker Witch', 'Weeping Wonderboy',
         'Boston Terrier of Terror',
         'Courier of Danger',
         'Mutant Mummer Zombie', 'Spasm Zombie', 'Scourge', 'Wolf-man Warg', 'Water Buffalo', 'Wham-a-Whama Rock Troll',
         'Woodland Spirit', 'Wraith', 'Wyvern', 'Murder of Crows', 'Lion-Eagle Hybrid', 'Apiarian Phantom'])

    def change_of(adjectives, monster, place_names):
        if 'of' in monster:
            print('The {} {} from {}'.format(adjectives, monster, place_names))
        else:
            print('The {} {} of {}'.format(adjectives, monster, place_names))

    # change_of(adjectives, monster)


if __name__ == "__main__":
    rat_king = Monster()
    rat_king.generate_monster(1)
    # print(rat_king.hp)
    # print(rat_king.magic)
