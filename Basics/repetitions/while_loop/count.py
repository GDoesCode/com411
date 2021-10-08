count = 0
num = int(input("How many cables should I avoid?\n"))

while count < num:
    print("Avoiding...", end="")
    count += 1
    print(f"Done! {count} live cable avoided!")

print("All live cables have been avoided.")