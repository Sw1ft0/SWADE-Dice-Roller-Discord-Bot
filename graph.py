import itertools
import tokenizer


class Edge:
    id_iter = itertools.count()

    def __init__(self, from_id, to_id, condition):
        self.name = "type"
        self.id = next(self.id_iter)
        self.from_id = from_id
        self.to_id = to_id
        self.condition = condition


class Node:
    id_iter = itertools.count()

    def __init__(self, name):
        self.name = name
        self.id = next(self.id_iter)
        self.out_edges: list[Edge] = []
        self.in_edges: list[Edge] = []

    def add_out_edge(self, to_id, condition):
        self.out_edges.append(Edge(self.id, to_id, condition))

    def get_id(self):
        return self.id

    def get_edge(self, token: tokenizer.Token):
        for edge in self.out_edges:
            if token.type == edge.name:
                return edge

    def snake_case(self, token: tokenizer.Token):
        edge = self.get_edge(token)
        return edge
