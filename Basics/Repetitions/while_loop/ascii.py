count = ""
num = int(input("How many bars should be charged?\n"))

while len(count) < num:
    print("Charging:")
    count += "|"
    print(count)

print("The battery is fully charged")