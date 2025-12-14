import numpy as np


def parse_help(help_str: str) -> dict[str, list[int]]:
    """
    Parse the bonifiers to the dice roll
    """

    help_list = help_str.split()

    # Parsed help dictionary
    parsed: dict[str, list[int]] = {"flat": [], "dice": []}

    # TODO: Maybe check for correct input?
    for help in help_list:
        if "d" in help:
            number, _type = [int(x) for x in help.split("d")]
            parsed["dice"] += [_type for i in range(number)]
        else:
            parsed["flat"].append(int(help))

    return parsed


def main() -> None:
    """
    Calculate the odds to beat a particular challenge
    """

    n_tries = int(1e6)
    die_type = 20

    # Maximum probability (e.g. if critical failures are allowed)
    max_probability = 95

    # Minimum probability (e.g. if critical successes are allowed)
    min_probability = 5

    print(f"Using a d{die_type}")
    challenge = int(input("Input DC: "))
    advantage_str = input("Advantage or disadvantage (a/d)? Leave blank if none: ")
    double_dice = advantage_str == "a" or advantage_str == "d"

    # Cast the dice and sort
    dice = np.random.choice(die_type, size=n_tries) + 1
    if double_dice:
        dice_second = np.random.choice(die_type, size=n_tries) + 1
        if advantage_str == "a":
            dice = np.maximum(dice, dice_second)
        else:
            dice = np.minimum(dice, dice_second)

    help_list = parse_help(input("Add the bonifiers separated by spaces: "))

    for f in help_list["flat"]:
        dice += f
    for d in help_list["dice"]:
        dice += np.random.choice(d, size=n_tries) + 1

    # Find the index where the challenge is
    dice = np.sort(dice)
    index = np.searchsorted(dice, challenge, side="left")

    # Calculate probabilities
    probability = max(min(float((1 - index / n_tries)) *
                          100, max_probability), min_probability)

    print(f"The probability of beating the odds is {probability:.2f}%")


if __name__ == "__main__":
    main()
