import tokenizer
from abc import ABC, abstractmethod


class Condition(ABC):

    @abstractmethod
    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        pass


class RegexKeyword(Condition):

    def __init__(self):
        self.regex: str = r'(?i)d(ice)?'

    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        del self
        if token.type == 'KEYWORD':
            return True
        return False


class TokenKind(Condition):

    def __init__(self, kind: str):
        self.kind = kind

    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        pass


class PositiveInt(Condition):

    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        pass


class Operator(Condition):

    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        pass


class Any(Condition):

    def satisfies_condition(self, token: tokenizer.Token) -> bool:
        pass