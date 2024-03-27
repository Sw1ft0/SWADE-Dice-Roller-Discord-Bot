from typing import NamedTuple
import re
import main


class Token(NamedTuple):
    type: str
    value: str
    position: int


keywords = {'d', 'D', 'dice', 'DICE'}


def tokenize(command):
    token_specification = [
        ('NUMBER',   r'\d+'),   # Integer number
        ('WORD',       r'[A-Za-z]+'),     # Identifiers
        ('OP',       r'[+\-*/]'),       # Arithmetic operators
        ('SKIP',     r'[ \t]+'),        # Skip over spaces and tabs
        ('MISMATCH', r'.'),             # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_start = 0
    for mo in re.finditer(tok_regex, command):
        kind: str | None = mo.lastgroup
        value: int | str = mo.group()
        position = mo.start() - line_start
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'WORD' and value in keywords:
            kind = value
        elif kind == 'WORD':
            raise ValueError(f'{value!r} unexpected')
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        yield Token(str(kind), str(value), position)


def roll_with_tokenizer(command):
    x = tokenize(command)
    keyword_indicator = False
    quantity: int = 1
    result_line: str = f'Result of rolling {command} is '
    for i, token in enumerate(x):
        if token.type in keywords:
            keyword_indicator = True
        elif token.type == 'NUMBER' and keyword_indicator:
            for j in range(quantity):
                result_line += f'{main.solve(int(token.value))}'
                if j != quantity - 1:
                    result_line += f' + '
            quantity = 1
            keyword_indicator = False
        elif token.type == 'NUMBER' and not keyword_indicator:
            quantity = int(token.value)
        elif token.type == 'OP' and token.value == '+':
            result_line += f' + '
    return result_line
