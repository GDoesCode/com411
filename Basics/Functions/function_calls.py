complete = False


def display_in_a_box(word):
    for i in range(len(word) + 2):
        print("-", end="")
    print(f"\n|{word}|")
    for i in range(len(word) + 2):
        print("-", end="")


def display_lower_case(word):
    print(word.lower())


def display_upper_case(word):
    print(word.upper())


def display_mirrored(word):
    print(word + " | " + word[len(word)::-1])


def repeat():
    repeats = int(input("How many times would you like it to repeat?\n"))
    for i in range(repeats):
        if (i % 2) == 0:
            print(word.lower())
        else:
            print(word.upper())


word = str(input("Please enter a word:\n"))
while not complete:
    option = input("Please choose an option:\n"  # want int
                   "1) Display in a Box\n"  # display the word in an ascii art box
                   "2) Display Lower-case\n"  # display the word in lower-case e.g. hello
                   "3) Display Upper-case\n"  # display the word in upper-case e.g. HELLO
                   "4) Display Mirrored\n"  # display the word with its mirrored word e.g. Hello | olleH
                   "5) Repeat\n")  # ask the user how many times to display the word and then display the word that
                                   # many times alternating between upper-case and lower-case
    if option == "1":
        display_in_a_box(word)
        complete = True
    elif option == "2":
        display_lower_case(word)
        complete = True
    elif option == "3":
        display_upper_case(word)
        complete = True
    elif option == "4":
        display_mirrored(word)
        complete = True
    elif option == "5":
        repeat()
        complete = True
    else:
        print("Error: Input not recognised\n")