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
    selected_option = int(input("\nPlease select one of the following options:\n"
                                "[1] Display the names of all passengers\n"
                                "[2] Display the number of passengers that survived\n"
                                "[3] Display the number of passengers per gender\n"
                                "[4] Display the number of passengers per age group\n"))
    return selected_option


def display_passenger_names():
    print("\nThe names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = record[1]
        if survival_status == "1":
            num_survived += 1
    print(f"\n{num_survived} passengers survived")


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1
    print(f"\nFemales: {females}, males: {males}")


def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()
