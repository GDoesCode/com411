class Robot:
    # region Class (Constant) attributes
    MAX_ENERGY = 100

    # endregion

    # region Initialiser
    def __init__(self, name="Robot", age=0, energy=0):
        # region Instance attributes
        self.name = name
        self.age = age
        self.energy = energy

        # endregion

    # endregion

    # Instance methods
    def display(self):
        print(f"I am {self.name}")

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if (self.energy + amount) <= Robot.MAX_ENERGY:
            self.energy += amount
        else:
            self.energy = Robot.MAX_ENERGY

    def move(self, distance):
        if (self.energy - distance) <= 0:
            self.energy = 0
        else:
            self.energy -= distance

    # endregion

    # region Magic methods
    def __repr__(self):
        return f"robot(name={self.name}, age={self.age})"

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old."

    # endregion


if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(robot.__repr__())
    print(robot.__str__())
    robot.eat(50)
    print(robot.energy)
    robot.eat(100)
    print(robot.energy)
    robot.move(20)
    print(robot.energy)
    robot.move(100)
    print(robot.energy)
