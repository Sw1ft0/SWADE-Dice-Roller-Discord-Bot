# /d4 : return number from 1 to 4.
# /d6 : return number from 1 to 6.
# /d8 : return number from 1 to 8.
# /d10 : return number from 1 to 10.
# /d12 : return number from 1 to 12.
import random

command12 = "2dice12+1d4+3dice6"


def roll_dice(command: str) -> str:
    symbol: str
    dice: str
    prefix: str
    result_line: str = f'Result of rolling {command} is '
    dices_list: list[str] = command.split('+')
    for i, dice in enumerate(dices_list):
        prefix = dice[:dice.find('d')]
        dice = dice.removeprefix(prefix)
        if dice.startswith("dice"):
            dice = dice.removeprefix("dice")
        elif dice.startswith("d"):
            dice = dice.removeprefix("d")
        else:
            return "Error. Invalid command"
        for symbol in dice:
            if not symbol.isdigit():
                return 'Error. Wrong input: only numbers are allowed after "d" or "dice"'
        for symbol in prefix:
            if not symbol.isdigit():
                return 'Error. Wrong input: only numbers are allowed in prefix'
        if prefix == '0':
            return 'Error. Prefix can`t be 0'
        if len(prefix) == 0:
            prefix = '1'
        for j in range(int(prefix)):
            result_line += f'{solve(int(dice))}'
            if j != int(prefix)-1 or i != len(dices_list) - 1:
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
