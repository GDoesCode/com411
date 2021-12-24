import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings.append(next(csv_reader))
        for line in csv_reader:
            records.append(line)
    print("Done!")


def display_menu():
    selected_option = int(input("Please select one of the following options:\n"
                                "[1] Display the names of all passengers\n"
                                "[2] Display the number of passengers that survived\n"
                                "[3] Display the number of passengers per gender\n"
                                "[4] Display the number of passengers per age group\n"))
    return selected_option


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.\n")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")


if __name__ == "__main__":
    run()
