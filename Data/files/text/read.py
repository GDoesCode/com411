def display_chars(path, num_of_chars):
    print(f"The first {num_of_chars} characters are:")
    with open(path, "r") as file:
        print(file.readline(num_of_chars))
    print()


def display_line(path):
    print("The first line is:")
    with open(path, "r") as file:
        print(file.readline())


def display_text(path):
    print("The full text is:")
    with open(path, "r") as file:
        print(file.read())


def run():
    num = int(input("How many characters to read?\n"))
    display_chars("library.txt", num)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()