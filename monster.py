from random import randrange
#
class Monster:
    '''this is intended as a base attribute list for our monsters'''
    def __init__(self, hp, strength, armor, magic): '''be sure to add weapons back into the function down the road.  
    add attribute position which will be a list where 0 = y & 1 = x.  this will be come clear later.'''
        self.mode = 'ROAM' # also includes FIGHT when one must fight
        self.avatar =
        self.biom =
        self.hp = hp
        self.strength = strength
        self.armor = armor
        self.magic = magic
        self.m_typ = self.m_type()
        self.biom = self.m_typ



    def __str__(self):
        return 'hp: {}, strength: {}, armor: {}, magic: {}'.format(self.hp, self.strength, self.armor, self.magic)


    def m_type(self):
        return [
            (" §", ".,• º∞* xXX"),
            (" £", ".,•º ∞* xXX"),
            (" §", ".,•º ∞*:"),
            (" π", " ,º ∞* .;"),
            (" £", " .,*;"),
            (" ¥", ". •* xXX"),
            (" π", " .,•º∞*;"),
            (" ∫", ".,• º∞*;"),
            (" £", ".,•º∞*:"),
            (" ƒ", " .,•º∞*:"),
            (" §", ".,•º∞*: .")
        ][randrange(25)  % 10]






def generate_monster(level):
    '''generates a monster based on certain ranges corresponding to a level as determined at some later time'''
    hp = randrange(40,100) * level
    strength = randrange(60,100)
    armor = int(round((hp * strength) / 200, 0))
    magic = randrange(40,100)

    new_monster = Monster(hp, strength, armor, magic)
    print(new_monster)

generate_monster(1)




# rat_king = Monster(100, 20, 100, 5, 'sword', 3)
# print(rat_king.magic)



