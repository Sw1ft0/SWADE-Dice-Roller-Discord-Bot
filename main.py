import random

command12 = "d12"


def roll_dice(command: str) -> str:
    match command:

        case 'd4':
            return str(random.randint(1, 5))

        case 'd6':
            return str(random.randint(1, 7))

        case 'd8':
            return str(random.randint(1, 9))

        case 'd10':
            return str(random.randint(1, 11))

        case 'd12':
            return str(random.randint(1, 13))

        case _:
            return "Error. Wrong command."

print(roll_dice(command12))





