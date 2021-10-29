def directions():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn Left")
    directions.append("Turn Right")
    return directions


def run():
    print(directions())


if __name__ == "__main__":
    run()
