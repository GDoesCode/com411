class Human:
    # region Class (constant) attributes
    MAX_ENERGY = 100

    # end region

    # region Initialiser
    def __init__(self, name="Human", age=0):
        # region instance attributes
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

        # end region

    # endregion

    # region Instance methods
    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if (self.energy + amount) <= Human.MAX_ENERGY:
            self.energy += amount
        else:
            self.energy = Human.MAX_ENERGY

    def move(self, distance):
        if (self.energy - distance) <= 0:
            self.energy = 0
        else:
            self.energy -= distance

    # endregion

    # region Magic methods
    def __repr__(self):
        return f"human(name={self.name}, age={self.age})"

    def __str__(self):
        return f"Human {self.name} is {self.age} years old."

    # endregion


if __name__ == "__main__":
    human = Human()
    human.display()
    print(human.__repr__())
    print(human.__str__())
    human.move(20)
    print(human.energy)
    human.move(100)
    print(human.energy)
    human.eat(50)
    print(human.energy)
    human.eat(100)
    print(human.energy)
