import csv


def extract(path):
    print("\nExtracting...", end="")
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = str("")
        for lines in csv_reader:
            names += "\n" + lines[1]
    print(f"Done!\nThe extracted names are as follows:{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
