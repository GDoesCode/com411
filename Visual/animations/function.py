import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    print(f"Frame No.{frame}")


def run():
    anim = animation.FuncAnimation(fig,
                                   animate,
                                   frames=10,
                                   interval=1000,
                                   repeat=False)
    plt.show()


if __name__ == "__main__":
    run()