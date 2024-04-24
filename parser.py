import graph
import tokenizer
# from abc import ABC, abstractmethod
#
# StateID: int = 0
# StepResult: bool = False
#
#
# class Condition(ABC):
#
#     @abstractmethod
#     def satisfies_condition(self, token: tokenizer.Token) -> bool:
#         pass
#
#
# class RegexCondition(Condition):
#     regex: str
#
#     def satisfies_condition(self, token: tokenizer.Token) -> bool:
#         pass
#
#
# class HasDigitsCondition(Condition):
#     numbers: list[int]
#
#     def satisfies_condition(self, token: tokenizer.Token) -> bool:
#         pass
#
#
# class Edge:
#     from_id: StateID
#     to_id: StateID
#     condition: Condition
#
#
# class StateNode(Edge):
#     id: StateID
#     out_edges: list[Edge]
#     in_edges: list[Edge]
#
#     @staticmethod
#     def find_edge(self, token: tokenizer.Token) -> Edge | None:
#         pass
#
#
# class StateMachine(StateNode):
#     nodes: list[StateNode]
#     current_state: StateID
#
#     @staticmethod
#     def move_one_step(self, token: tokenizer.Token) -> StepResult:
#         pass


class StateMachine:

    def __init__(self, nodes: list[graph.Node], current_state: graph.Node):
        self.nodes: list[graph.Node] = nodes
        self.current_state: graph.Node = current_state

    def move_one_step(self, token: tokenizer.Token):
        i = False
        for node in self.nodes:
            if i:
                self.current_state = node
                break
            if node == self.current_state:
                i = True

    def get_current_state(self):
        return self.current_state.id
