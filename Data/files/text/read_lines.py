def search(path):
    print("\nSearching...")
    with open(path, "r") as file:
        for line in file:
            print(f"Looked in {line}")
    print("\n...Done!")


def run():
    search("library.txt")


if __name__ == "__main__":
    run()
