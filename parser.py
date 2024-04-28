import graph
import tokenizer


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
