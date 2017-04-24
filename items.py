class Items:
    def __init__(self, name, type, effect, weight, lvl):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight
        self.level = lvl

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.title(), self.effect,
                                                                self.weight)

    def __repr__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.title(), self.effect,
                                                                self.weight)

if __name__ == '__main__':
    pass
