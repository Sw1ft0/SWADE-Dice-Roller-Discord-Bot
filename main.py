import random

command12 = "d12"


def roll_dice(command: str) -> str:
    d_counter: int = 0
    num: str = ''
    symb: str
    for symb in command:
        if symb.isdigit() and d_counter == 1:
            num = num + symb
        elif symb == 'd':
            d_counter = d_counter + 1
        else:
            return f"Error. Wrong input: only 1 \'d\' letter possible but it is {d_counter}"
    return 'Result: ' + str(random.randint(1, int(num)))

print(roll_dice(command12))





