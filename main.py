# /d4 : return number from 1 to 4.
# /d6 : return number from 1 to 6.
# /d8 : return number from 1 to 8.
# /d10 : return number from 1 to 10.
# /d12 : return number from 1 to 12.
import random

command12 = "dice12+d4+dice6"


def roll_dice(command: str) -> str:
    num: str = ''
    symbol: str
    dice: str
    result_line: str = f'Result of rolling {command} is '
    dices_list: list[str] = command.split('+')
    for i, dice in enumerate(dices_list):
        if dice.startswith("dice"):
            dice = dice.removeprefix("dice")
        elif dice.startswith("d"):
            dice = dice.removeprefix("d")
        else:
            return "Error. Invalid command"
        for symbol in dice:
            if not symbol.isdigit():
                return 'Error. Wrong input: only numbers are allowed after d'
        result_line += f'{solve(int(dice))}'
        if i != len(dices_list) - 1:
            result_line += f' + '
    return result_line


def solve(num: int) -> str:
    roll_result: int = random.randint(1, int(num))
    dice_result: int = roll_result
    while roll_result == int(num):
        roll_result = random.randint(1, int(num))
        dice_result += roll_result
    return str(dice_result)


print(roll_dice(command12))