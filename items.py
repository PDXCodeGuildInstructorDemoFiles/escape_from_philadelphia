import random


class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight


def weapon(effect):
    names = ['sword of might', 'wooden sword']
    return Items(random.choice(names), 'weapon', effect, random.randrange(5, 10))


def armor(self, name, type, effect, weight):
    self.name = name
    self.type = type
    self.effect = effect
    self.weight = weight


def first_aid(self, name, type, effect, weight):
    self.name = name
    self.type = type
    self.effect = effect
    self.weight = weight


sword = weapon(-20)

print(sword.name)
print(sword.weight)

