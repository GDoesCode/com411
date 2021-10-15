def display_ladder(steps):
    print("|    |")
    for i in range(steps):
        print("******\n"
              "|    |")


def create_ladder():
    steps = int(input("How many steps are on the ladder?\n"))
    display_ladder(steps)


create_ladder()