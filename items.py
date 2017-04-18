class Items:
    def __init__(self, name, type, effect, weight):
        self.name = name
        self.type = type
        self.effect = effect
        self.weight = weight

    def __str__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect,
                                                                self.weight)

    def __repr__(self):
        return 'Name: {} Type: {} Effect: {} Weight: {}'.format(self.name.title(), self.type.capitalize(), self.effect,
                                                                self.weight)

