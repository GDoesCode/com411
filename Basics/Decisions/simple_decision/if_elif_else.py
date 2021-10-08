print("What direction should Beep move in (up, down, left or right)?")
direction = str(input())
complete = "false"
while complete == "false":
    if direction == "up":
        print("Beep is painting in the upward direction!")
        complete = "true"
    elif direction == "down":
        print("Beep is painting in the downward direction!")
        complete = "true"
    elif direction == "left":
        print("Beep is painting in the left direction!")
        complete = "true"
    elif direction == "right":
        print("Beep is painting in the right direction!")
        complete = "true"
    else:
        print("Please help Beep choose a valid direction!")
        direction = str(input())
