import tokenizer


class Any:
    pass


class RegexKeyword:

    def __init__(self):
        self.regex: str = r'(?i)d(ice)?'

    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        del self
        if token.type == 'KEYWORD':
            return True
        return False


class TokenKind:

    def __init__(self, kind: str):
        self.kind = kind


class PositiveInt:
    pass


class Operator:
    pass
