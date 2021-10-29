def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run():
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")


if __name__ == "__main__":
    run()
