def directions():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction


def menu():
    print("Please select a direction:")
    direction = directions()
    for i in range(len(direction)):
        print(f"{i}: {direction[i]}")


def run():
    menu()


if __name__ == "__main__":
    run()
