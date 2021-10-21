rows = int(input("How many rows should I have?\n"))
columns = int(input("\nHow many columns should I have?\n"))

for i in range(rows):
    for j in range(columns):
        print(":-)", end="")
    print()

print("\nDone!")
