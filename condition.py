class RegexKeyword:

    def __init__(self, regex: str):
        self.regex = regex


class Any:
    pass


class TokenKind:

    def __init__(self, kind: str):
        self.kind = kind


class PositiveInt:
    pass


class Operator:
    pass
