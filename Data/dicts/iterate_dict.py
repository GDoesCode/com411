def display_keys(data):
    print("\nKeys:")
    for key in data.keys():
        print(key)


def display_values(data):
    print("\nValues:")
    for value in data.values():
        print(value)


def display_items(data):
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def run():
    print(f"Dictionary:\n{pattern()}\n")
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


if __name__ == "__main__":
    run()
