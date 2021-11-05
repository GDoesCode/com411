def observed():
    observations = []
    for i in range(5):
        observation = str(input("Enter an observation:\n"))
        observations.append(observation)
    return observations


def remove_observations(observations):
    answer = str(input("Would you like to remove observations?\n"))
    while answer == "yes" or answer == "y":
        remove_observation = str(input("What observation would you like to remove?\n"))
        observations.remove(remove_observation)
        answer = str(input("Would you like to remove observations?\n"))


def run():
    observations = observed()
    remove_observations(observations)

    # populate set
    observations_set = set()
    for observation in observations:
        observations_set.add((observation, observations.count(observation)))

    # print set
    print("Observations:")
    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times")


if __name__ == "__main__":
    run()
