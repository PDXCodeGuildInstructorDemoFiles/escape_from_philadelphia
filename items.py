import random


class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect, self.weight)


def weapon(effect):
    """This function generates a random weapon with random weight"""
    w_names = ['sword of might', 'wooden sword', 'big axe', 'dagger']
    return Items(random.choice(w_names), 'weapon', effect, random.randrange(5, 10))


def armor():
    """This function generates a random piece of armor with random effect (defense) and weight"""
    a_names = ('steel chest plate', 'iron helmet', 'leather gloves', 'spiked helmet')
    return Items(random.choice(a_names), 'armor', random.randrange(1, 50), random.randrange(5, 20))

def first_aid():
    """This function generates random first aid items of random effect (healing). All weigh one pound"""
    fa_names = ['cake', 'cheesesteak', 'water', 'potion', 'coffee', "soft pretzels"]
    return Items(random.choice(fa_names), 'first aid', random.randrange(1, 40), 1)



#Character item selection (possibly add this to inventory.py...?):
#First aid item would add 1 pound from inventory when picked up, subtract 1 pound when used, add to health when used
#Weapon would add variable pounds when picked up, subtract those pounds when dropped, subtract from opponent's health
#Armor adds variable pounds when picked up, subtracts pounds when dropped, decreases impact (divide

#helmet = armor(10)
#sword = weapon(-20)

print(armor())
print(first_aid())
#print(helmet)

