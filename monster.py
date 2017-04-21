from random import randrange, choice
#
class Monster:
    '''this is intended as a base attribute list for our monsters'''
    def __init__(self, hp, strength, armor, magic):
        """be sure to add weapons back into the function down the road.  
        add attribute position which will be a list where 0 = y & 1 = x.  
        this will be come clear later."""

        self.mode = None #'ROAM' also includes 'FIGHT' when one must fight - function to follow?
        self.avatar = None
        self.hp = hp
        self.strength = strength
        self.armor = armor
        self.magic = magic
        # self.m_typ = self.m_type() #touch base with Joe re: this and the succeeding attribute
        # self.biom = self.m_typ

    def __str__(self):
        return 'hp: {}, strength: {}, armor: {}, magic: {}'.format(self.hp, self.strength, self.armor, self.magic)


    def generate_monster(level):
        '''generates a monster based on certain ranges corresponding to a level as determined at some later time'''
        hp = randrange(40,100) * level
        strength = randrange(60,100)
        armor = int(round((hp * strength) / 200, 0))
        magic = randrange(40,100)

        # new_monster = Monster(hp, strength, armor, magic)

    generate_monster(1)



    adjectives = choice(['aggravating', 'annoying', 'distressing', 'disturbing', 'inconvenient', 'arduous', 'backbreaker',
                'bothersome', 'troublesome', 'irritating', 'troublesome', 'vexing', 'exasperating',
                'incommodious', 'remote', 'vexatious', 'ambitious', 'demanding', 'difficile', 'effortful', 'exacting',
                'wearisome', 'formidable', 'galling', 'onerous', 'operose', 'painful', 'problem', 'problematic',
                'prohibitive', 'rigid', 'severe', 'strenuous', 'titanic', 'toilsome', 'tough', 'trying', 'unyielding', 'uphill',
                'burdensome', 'challenging', 'crucial', 'gargantuan', 'heavy', 'herculean', 'immense', 'irritating',
                'labored', 'laborious'])

    place_names = choice(['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',
                'Manayunk Railroad Yard','Skidoo Water Park Palace', 'Dunks Ferry Playground', 'Pigeons\' Gauntlet',
                'the Inauspicious Tower of Dread at Mario Lanza Boulevard', 'the Dungeon at Dicks Ave.',
                'the Reading Terminal Market Book Club', 'the Stronghold of Doom at Longwood Gardens',
                'the cave under the Philadelphia Zoo', 'the dreaded Eastern State Penitentiary',
                'the depressing, perenial dissapointment known as the Philadelphia Eagles'])

    monster = choice(['Rabbit', 'Troll', 'Dragon', 'Carniverous Camel', 'Loner Llama', 'Ogre', 'Slime Mold', 'Fungal Beast',
                    'Vampire', 'Dampyr', 'malformed non-specific animal', 'Shark Rocket', 'Tengu', 'Shadow Liger', 'Dragon', 'Gaslich',
                    'Hollowlich', 'Embermask', 'Bowelwraith', 'Clammy-hand Creeper', 'Creepy Cuddler', 'Mutant Tortoises of Terror',
                    'Gregarious Geek', 'Lurking Llamas', 'Horrible Screaker Witch', 'Weeping Wonderboy', 'Boston Terrier of Terror',
                    'Courier of Danger',
                    'Mutant Mummer Zombie', 'Spasm Zombie', 'Scourge', 'Wolf-man Warg', 'Water Buffalo', 'Wham-a-Whama Rock Troll',
                    'Woodland Spirit', 'Wraith', 'Wyvern', 'Murder of Crows', 'Lion-Eagle Hybrid', 'Apiarian Phantom'])

    def change_of(adjectives, monster, place_names):
        if 'of' in monster:
            print('The {} {} from {}'.format(adjectives, monster, place_names))
        else:
            print('The {} {} of {}'.format(adjectives, monster, place_names))


    change_of(adjectives, monster, place_names)


# rat_king = Monster(100, 20, 100, 5, 'sword', 3)
# print(rat_king.magic)



