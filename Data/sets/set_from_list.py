def observed():
    observations = []
    for i in range(7):
        observation = str(input("Please enter an observation (enter a value twice):\n"))
        observations.append(observation)
    return observations


def run():
    print("Counting observations...")
    observed_list = observed()
    observed_set = set()
    for i in range(len(observed_list)):
        observed_set.add((observed_list[i], observed_list.count(observed_list[i])))
    print(observed_set)


if __name__ == "__main__":
    run()
