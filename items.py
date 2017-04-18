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
    w_names = ['sword of might', 'wooden sword', 'big axe', 'dagger']
    return Items(random.choice(w_names), 'weapon', effect, random.randrange(5, 10))


def armor():
    a_names = ('steel chest plate', 'iron helmet', 'leather gloves', 'spiked helm')
    return Items(random.choice(a_names), 'armor', random.randrange(1, 50), random.randrange(5, 20))

def first_aid(self, name, type, effect, weight):
    self.name = name
    self.type = type
    self.effect = effect
    self.weight = weight

helmet = armor()
sword = weapon(-20)

print(sword)
print(helmet)

