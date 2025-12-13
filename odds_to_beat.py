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
            number, _type = help.split("d")
            int_number = int(number)
            int_type = int(_type)
            parsed["dice"] += [int_type for i in range(int_number)]
        else:
            parsed["flat"].append(int(help))

    return parsed


def main() -> None:
    """
    Calculate the odds to beat a particular challenge
    """

    n_tries = int(1e6)
    die_type = 20

    print(f"Using a d{die_type}")
    challenge = int(input("Input difficulty class: "))

    # Cast the dice and sort
    dice = np.random.choice(die_type, size=n_tries) + 1

    help_list = parse_help(input("Add the bonifiers separated by spaces: "))

    for f in help_list["flat"]:
        dice += f
    for d in help_list["dice"]:
        dice += np.random.choice(d, size=n_tries) + 1

    # Find the index where the challenge is
    dice = np.sort(dice)
    index = np.searchsorted(dice, challenge, side="left")

    # Calculate probabilities
    percent = (1 - index / n_tries) * 100
    s = f"The probability of beating the odds is {percent:.2f}%"
    print(s)


if __name__ == "__main__":
    main()
