# Odds to beat

## Description

This python script uses a Monte Carlo calculation to calculate the odds to beat
a particular dice throw in DnD. Upon using, it prompts the user for a
difficulty class (DC) to beat, wehther they have advantage-like modifiers, and
then a bonifiers list, which can be either flat or specified in the typical die
format (`XdY`, where `X` is the number of dice and `Y` is their value).
The bonifiers can be negative.

This is an example on how to use the code to calculate the odds to beat a `18
DC` with a `3d4 + 1` modifier

```sh
python3 odds_to_beat.py
Using a d20
Input DC: 18 
Advantage or disadvantage (a/d)? Leave blank if none:
Add the bonifiers separated by spaces: 1 3d4
The probability of beating the odds is 57.47%
```

Same example with disadvantage:

```sh
python3 odds_to_beat.py
Using a d20
Input DC: 18
Advantage or disadvantage (a/d)? Leave blank if none: d
Add the bonifiers separated by spaces: 1 3d4
The probability of beating the odds is 33.88%
```

## Hardcoded values

Currently the main die value is hardcoded to `1d20`, and the number of Monte
Carlo tries is hardcoded to `1e6`.

## Dependencies

See `requirements.txt`
