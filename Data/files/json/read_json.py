import json


def read(path):
    with open(path) as file:
        data = json.load(file)
        city_name = data["city"]
        population = data["population"]
        print(f"City Name: {city_name}\n"
              f"Population Size: {population}")
        bots = data["bots"]
        for bot in bots:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()
