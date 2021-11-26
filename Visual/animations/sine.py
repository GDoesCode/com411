import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = range(0, frame)
    y = []
    y = [math.sin(math.radians(degrees)) for degrees in x]
    ax.plot(x, y)


def run():
    some_animation = animation.FuncAnimation(fig,
                                             animate,
                                             frames=720,
                                             interval=100)
    plt.show()


if __name__ == "__main__":
    run()
