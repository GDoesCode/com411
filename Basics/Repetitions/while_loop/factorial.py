num = int(input("Please enter a number:\n"))
count = 1
factorial_of_num = num

while num != count:
    factorial_of_num = factorial_of_num * count
    count += 1

print(f"\nThe factorial of {num} is {factorial_of_num}")
