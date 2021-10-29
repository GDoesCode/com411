def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    direction = []
    steps = []
    for i in range(len(movements()) // 2):
        direction.append(movements()[(2 * i)])

    for i in range(len(movements()) // 2):
        steps.append(movements()[((2 * i) + 1)])

    for i in range(len(movements()) // 2):
        print(f"{direction[i]} for {steps[i]} steps")


if __name__ == "__main__":
    run()
