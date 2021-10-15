complete = False
print("Program Started!")
while not complete:
    code = int(input("Please enter an ASCII code:\n"))
    if code in range(32, 126):
        character = chr(code)
        print(f"The character represented by the ASCII code {code} is: {character}")
        complete = True
    else:
        print("Error: input not in range")
print("Program Ended!")