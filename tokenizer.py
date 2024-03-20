from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    position: int

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
        kind = mo.lastgroup
        value = mo.group()
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
        yield Token(kind, value, position)

keywords = {'d', 'D', 'dice', 'DICE'}
input = '2dice12+d6+1dice4'

if __name__ == '__main__':
    for token in tokenize(input):
        print(token)