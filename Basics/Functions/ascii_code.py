print("Program Started!")
complete = False
while not complete:
    character = input("Please enter a standard character.\n")
    if len(character) == 1:
        ascii_char = ord(character)
        print(f"The ASCII code for {character} is {ascii_char}")
    else:
        print("Error: character not detected")
print("Program Ended!")