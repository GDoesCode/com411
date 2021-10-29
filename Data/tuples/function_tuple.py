def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    min_likelihood = likelihood()[0]
    max_likelihood = likelihood()[1]
    print(f"Minimum likelihood of falling: {min_likelihood}%\n"
          f"Maximum likelihood of falling: {max_likelihood}%")


if __name__ == "__main__":
    run()
