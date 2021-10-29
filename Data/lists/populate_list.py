def directions():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction


def menu():
    print("Please select a direction:")
    direction = directions()
    for i in range(len(direction)):
        print(f"{i}: {direction[i]}")
    response = int(input())
    return direction[response]


def run():
    route = []
    print("Working out an escape route...")
    for i in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()
