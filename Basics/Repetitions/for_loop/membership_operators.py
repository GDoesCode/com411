phrase = str(input("What phrase do you see?\n"))
print("\nReversing...\n")
print("The phrase is: ", end="")

reversed_phrase = ""

for letter in phrase:
    reversed_phrase = letter + reversed_phrase

print(reversed_phrase)
