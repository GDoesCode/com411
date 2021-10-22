import csv


def export(path, num_exported_bots):
    print("Exporting...", end="")
    with open(path, "a") as file:
        for bot in range(num_exported_bots):
            bot_id = int(input("\nWhat is th id of the bot?\n"))
            bot_name = str(input("What is the name of the bot?\n"))
            bot_paint = str(input("What is the paint of the bot?\n"))
            data = f"{bot_id},{bot_name},{bot_paint}\n"
            file.write(data)
    print("Done!")


def run():
    num = int(input("How many bots would you like to import?\n"))
    export("exported_bots.csv", num)


if __name__ == "__main__":
    run()
