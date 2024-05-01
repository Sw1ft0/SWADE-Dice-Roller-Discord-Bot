import itertools
import tokenizer
import condition


class Edge:
    id_iter = itertools.count()

    def __init__(self, from_id: int, to_id: int, received_condition: condition.Condition):
        self.name: str = "type"
        self.id: int = next(self.id_iter)
        self.from_id: int = from_id
        self.to_id: int = to_id
        self.condition: condition.Condition = received_condition


class Node:
    id_iter = itertools.count()

    def __init__(self, name: str):
        self.name: str = name
        self.id: int = next(self.id_iter)
        self.out_edges: list[Edge] = []
        self.in_edges: list[Edge] = []

    def add_out_edge(self, to_id: int, received_condition: condition.Condition):
        self.out_edges.append(Edge(self.id, to_id, received_condition))

    def get_id(self):
        return self.id

    def get_edge(self, token: tokenizer.Token):
        for edge in self.out_edges:
            if token.type == edge.name:
                return edge

    def find_edge(self, token: tokenizer.Token):
        edge = self.get_edge(token)
        return edge
