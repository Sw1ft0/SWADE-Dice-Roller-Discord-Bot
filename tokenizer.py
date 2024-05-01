from typing import NamedTuple
import re
import main


class Token(NamedTuple):
    type: str
    value: str
    position: int


class Edge(NamedTuple):
    beginning_point: int
    token_type: str
    end_point: int


edge_list: list[Edge] = [
    Edge(0, 'SKIP', 0),
    Edge(0, 'NUMBER', 1),
    Edge(0, 'KEYWORD', 2),
    Edge(1, 'KEYWORD', 2),
    Edge(2, 'NUMBER', 3),
    Edge(3, '+', 0),
    Edge(3, 'SKIP', 3),
    Edge(3, 'EOE', 4),
]
print(edge_list)


def tokenize(command: str) -> Token:
    token_specification = [
        ('NUMBER', r'\d+'),  # Integer number
        ('KEYWORD', r'(?i)d(ice)?'),  # Identifiers
        ('OP', r'[+\-*/]'),  # Arithmetic operators
        ('SKIP', r'[ \t]+'),  # Skip over spaces and tabs
        ('MISMATCH', r'.'),  # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_start = 0
    for mo in re.finditer(tok_regex, command):
        kind: str | None = mo.lastgroup
        value: int | str = mo.group()
        position = mo.start() - line_start
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        yield Token(str(kind), str(value), position)


def roll_with_tokenizer(command: str) -> str:
    x = tokenize(command)
    keyword_indicator = False
    quantity: int = 1
    result_line: str = f'Result of rolling {command} is '
    for i, token in enumerate(x):
        if token.type == 'KEYWORD':
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
