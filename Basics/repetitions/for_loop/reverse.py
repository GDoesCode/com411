phrase = str(input("What phrase do you see?\n"))
print("\nReversing...\n")

print("The phrase is: ", end="")
for i in range(len(phrase)):
    print(f"{phrase[len(phrase) - (i + 1)]}", end="")
