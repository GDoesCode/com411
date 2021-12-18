import json


def read(path):
    print("Reading...", end="")
    with open(path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(path, save_data):
    print("Exporting...", end="")
    with open(path, "w") as file:
        json.dump(save_data, file)
    print("Done!")


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()
