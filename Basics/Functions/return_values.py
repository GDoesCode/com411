def sum_weights(weight_beep, weight_bop):
    weight_total = weight_beep + weight_bop
    return weight_total


def calc_avg_weight(weight_beep, weight_bop):
    weight_avg = sum_weights(weight_beep, weight_bop) / 2
    return weight_avg


def run():
    weight_beep = float(input("Please enter the weight of Beep:\n"))
    weight_bop = float(input("Please enter the weight of Bop:\n"))
    ans = str(input("Would you like to know their average or total weight?\n"))
    if ans == "total" or ans == "sum":
        print(f"The sum of Beep and Bop's weight is: {sum_weights(weight_beep, weight_bop)}")
    elif ans == "average" or ans == "avg":
        print(f"The average weight of Beep and Bop is: {calc_avg_weight(weight_beep, weight_bop)}")


run()