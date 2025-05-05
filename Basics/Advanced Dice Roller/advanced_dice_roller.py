# Advanced Dice Roller
# This script allows users to roll different types of dice (d4, d6, d8, d12, d20)
# and returns the result of the roll. It uses the random module to simulate the dice rolls.
# By Alexandros Panagiotakopoulos - alexandrospanag.github.io
# DATE: 5-05-2025

import random

def roll_dice(dice_type):
    """Rolls a dice of the given type and returns the result."""
    dice_sides = {
        "d4": 4,
        "d6": 6,
        "d8": 8,
        "d12": 12,
        "d20": 20
    }
    if dice_type not in dice_sides:
        raise ValueError("Invalid dice type. Choose from: d4, d6, d8, d12, d20.")
    return random.randint(1, dice_sides[dice_type])

if __name__ == "__main__":
    print("Advanced Dice Roller")
    print("Available dice: d4, d6, d8, d12, d20")
    dice = input("Which dice would you like to roll? (e.g., d6): ").strip().lower()
    try:
        result = roll_dice(dice)
        print(f"You rolled a {dice} and got: {result}")
    except ValueError as e:
        print(e)