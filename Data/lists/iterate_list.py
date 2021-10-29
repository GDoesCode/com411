def directions():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction


def menu():
    print("Please select a direction:")
    for i in range(len(directions())):
        print(f"{i}: {directions()[i]}")


def run():
    menu()


if __name__ == "__main__":
    run()
