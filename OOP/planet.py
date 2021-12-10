class Planet:

    def __init__(self, humans=None, robots=None):
        self.humans = []
        self.robots = []

    # region instance methods
    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    # endregion

    # region magic methods
    def __repr__(self):
        return f"Planet contains {len(self.humans)} humans: {self.humans} and {len(self.robots)} robots: {self.robots}"

    def __str__(self):
        return f"The Planet has {len(self.humans)} human inhabitants: {self.humans} and {len(self.robots)} robot inhabitants: {self.robots}"

    # endregion


if __name__ == "__main__":
    planet = Planet()
    planet.add_robot("Dave")
    planet.add_human("X562Y")
    robot_names = ["da Vinci Surgical System.", "KITT (Knight Rider)", "The Tachikomas (Ghost in the Shell)", "Toyota violin-playing robot.", "GERTY (Moon)", "Mega Man." "Rock 'Em Sock 'Em Robots.", "Doraemon."]
    for robot in robot_names:
        planet.add_robot(robot)
    print(planet.__repr__())
    print(planet.__str__())
