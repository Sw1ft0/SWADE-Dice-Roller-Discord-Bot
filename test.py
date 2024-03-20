import main
import tokenizer

command12 = "2dice12+d6+1dice4"

def roll_with_tokenizer(command):
    x = list(tokenizer.tokenize(command))
    indicator: int = 0
    quantity: int = 1
    result_line: str = f'Result of rolling {command} is '
    for i, token in enumerate(x):
        if token.type in tokenizer.keywords:
            indicator = 1
        elif token.type == 'NUMBER' and indicator:
            for j in range(quantity):
                result_line += f'{main.solve(token.value)}'
                if j != quantity - 1 or i != len(x) - 1:
                    result_line += f' + '
            quantity = 1
            indicator = 0
        elif token.type == 'NUMBER' and not indicator:
            quantity = token.value
    return result_line


print(roll_with_tokenizer(command12))
# print(main.roll_dice(command12))
