sequence = str(input("Please enter a sequence (marker then how many -'s then another marker at the end)\n"))
marker = str(input("Please enter the character for the marker\n"))
is_counting = False
count = 0

for position in sequence:
    if position == marker:
        if is_counting:
            is_counting = False
        else:
            is_counting = True
    elif (position != marker) & is_counting:
        count += 1

print(f"The distance between the markers is {count}")