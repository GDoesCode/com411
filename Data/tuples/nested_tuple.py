def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run():
    step = steps()
    good_steps = []
    bad_steps = []
    for i in step:
        if i[1] >= 50:
            bad_steps.append(step[i])
        else:
            good_steps.append(step[i])
    print(f"Good steps: {good_steps}, Bad steps: {bad_steps}")


if __name__ == "__main__":
    run()
