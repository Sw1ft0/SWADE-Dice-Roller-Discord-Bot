import random

command12 = "d12+d4"


def roll_dice(command: str) -> str:
    final_result: int = 0
    num: str = ''
    symbol: str
    index: int = len(command)
    result_line: str = f'Result of rolling {command} is '
    if command[0] != 'd':
        return 'Error. Invalid command'
    for symbol in command[1:]:
        if symbol.isdigit():
            num = num + symbol
        elif symbol == '+':
            index = command.find(symbol) + 1
            result_line += roll_dice(command[index:])
            break
        else:
            return "Error. Wrong input: only numbers are allowed after d"
    roll_result: int = random.randint(1, int(num))
    dice_result: int = roll_result
    while roll_result == int(num):
        roll_result = random.randint(1, int(num))
        dice_result += roll_result
    if index == len(command):
        return result_line
    else:
        return str(dice_result)

print(roll_dice(command12))