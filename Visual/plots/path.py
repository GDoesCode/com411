import matplotlib.pyplot as plt


def coordinate():
    x = int(input("Please enter an x value:\n"))
    y = int(input("Please enter an y value:\n"))
    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return x_values, y_values


def run():
    values = path()
    plt.plot(values[0], values[1], "r--o")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()


if __name__ == "__main__":
    run()