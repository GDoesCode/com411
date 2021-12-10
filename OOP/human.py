class Human:
    # region Class (constant)
    MAX_ENERGY = 100

    # region Initialiser
    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    # endregion

    # region Instance methods
    def display(self):
        print(f"I am {self.name}")

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
