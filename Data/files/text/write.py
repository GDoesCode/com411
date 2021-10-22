def search(path):
    print("\nSearching...", end="")
    sections = str("")
    books = str("Books:\n")
    with open(path, "r") as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")
    return f"{sections}\n\n{books}"


def save(path, data):
    print("Saving...", end="")
    with open(path, "w") as file:
        file.write(data)
    print("Done!")


def run():
    data = search("books.txt")
    save("section-books.txt", data)


if __name__ == "__main__":
    run()
