import csv


def read(path):
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        print(f"Headings:\n{next(csv_reader)}\n"
              f"Values:")
        for values in csv_reader:
            print(values)


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()