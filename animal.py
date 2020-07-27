

class Animal():
    pet = bool

    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def is_food(self):
        if self.pet:
            return '{} are not food'.format(self.name)
        else:
            return '{} are food'.format(self.name)


pigs = Animal('pigs', False)
cats = Animal('cats', True)


print(pigs.is_food())
print(cats.is_food())
