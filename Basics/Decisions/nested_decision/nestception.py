ans = str(input("Where should I look?\n"))

if ans == "in the bedroom":
    ans2 = str(input("Where in the bedroom should I look?\n"))
    if ans2 == "under the bed":
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")
elif ans == "in the bathroom":
    ans2 = str(input("Where in the bathroom should I look?\n"))
    if ans2 == "in the bathtub":
        print("Found a rubber duck but no battery.")
    else:
        print("Found a wet surface but no battery.")
elif ans == "in the lab":
    ans2 = str(input("Where in the lab should I look?\n"))
    if ans2 == "on the table":
        print("Yes! I found the battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but Iin will keep looking.")