import matplotlib.pyplot as plt
import random


def data():
    line_type = str(input("What type of line would you like (:, -- or -)?\n"))
    colour = str(input("What colour would you like (r, g or b)?\n"))
    marker = str(input("What style of marker would you like (o, s or ^)?\n"))
    path = {"Line style": line_type, "Colour": colour, "Marker style": marker}
    return path


def generate():
    lines = int(input("How many lines would you like to display?\n"))
    for i in range(lines):
        values = data()
        x = random.sample(range(0, 10), 5)
        y = random.sample(range(0, 10), 5)
        format_values = f"{values['Colour']}{values['Line style']}{values['Marker style']}"  # or use **values
        plt.plot(x, y, format_values)
    plt.show()


def run():
    print("Running...")
    generate()
    print("Done")


if __name__ == "__main__":
    run()
