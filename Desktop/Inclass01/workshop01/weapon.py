class Weapon:
    def __init__(self, name, type, level=1):
        self.name = name
        self.type = type
        self.level = level

    def upgrade(self):
        self.level += 1

    def display(self):
        print(f"Weapon Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Level: {self.level}")
