caps = str(input("Should I write in CAPS?\n"))
newline = str(input("Should I use a newline or space?\n"))
question = str(input("What question should I ask you (name or age)?\n"))

if caps == "yes" and newline == "yes":
    if question == "name":
        name = str(input("HELLO\nWHAT\nIS\nYOUR\nNAME?\n"))
        print(f"HELLO\n{name.upper()}!")
    else:
        age = int(input("HELLO\nWHAT\nIS\nYOUR\nAGE?\n"))
        print(f"YOU\nARE{age}\nYEARS\nOLD!")
elif caps == "no" and newline == "yes":
    if question == "name":
        name = str(input("hello\nwhat\nis\nyour\nname?\n"))
        print(f"hello\n{name.lower()}!")
    else:
        age = int(input("hello\nwhat\nis\nyour\nage?\n"))
        print(f"you\nare\n{age}\nyears\nold!")
elif caps == "yes" and newline == "no":
    if question == "name":
        name = str(input("HELLO WHAT IS YOUR NAME?\n"))
        print(f"HELLO {name.upper()}!")
    else:
        age = int(input("HELLO WHAT IS YOU AGE?\n"))
        print(f"YOU ARE {age} YEARS OLD!")
else:
    if question == "name":
        name = str(input("hello what is your name?\n"))
        print(f"hello {name.lower()}!")
    else:
        age = int(input("hello what is your age?\n"))
        print(f"you are {age} years old!")