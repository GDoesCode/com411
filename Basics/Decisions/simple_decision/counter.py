num1 = int(input("Enter the first whole number:\n"))
num2 = int(input("Enter the second whole number:\n"))
num3 = int(input("Enter the third whole number:\n"))
count = 0

if (num1/2).is_integer():
    count += 1
elif (num2/2).is_integer():
    count += 1
elif (num3/2).is_integer():
    count += 1

print(f"There were {count} even and {3 - count} odd numbers")