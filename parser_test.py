import unittest

import parser


class TestGraphNodes(unittest.TestCase):
    def test_node_creation(self):
        some = graph.Node('some')
        another = graph.Node('another')

    def test_node_connection(self):
        some = graph.Node('some')
        another = graph.Node('another')
        some.add_out_edge(another.get_id(), condition.Any())

    def test_finding_edge(self):
        some = graph.Node('some')
        another = graph.Node('another')
        some.add_out_edge(another.get_id(), condition.Any())

        found_edge = some.FindEdge(
            tokenizer.Token('type', 'value', 'position'))

        self.assertIsNotNone(found_edge)

    def test_state_machine_creation(self):
        some = graph.Node('some')
        another = graph.Node('another')
        parser.StateMachine([some, another], some)

    def test_state_machine_moving(self):
        some = graph.Node('some')
        another = graph.Node('another')
        some.add_out_edge(another.get_id(), condition.Any())
        state_machine = parser.StateMachine([some, another], some)

        state_machine.move_one_step(Token('type', 'value', 'position'))

        self.assertEqual(state_machine.get_current_state(), another.get_id())

    def test_dice_roller_parser_graph_creation(self):
        init = graph.Node('init')
        dice_count = graph.Node('dice count')
        dice_word = graph.Node('dice word')
        eoe = graph.Node('end of expression')

        dice_condition = condition.RegexKeyword(r'(?i)d(ice)?')

        init.add_out_edge(init.get_id(), condition.TokenKind('SKIP'))
        init.add_out_edge(dice_count.get_id(), condition.PositiveInt())

        init.add_out_edge(dice_word.get_id(), dice_condition)
        dice_count.add_out_edge(dice_word.get_id(), dice_condition)

        dice_word.add_out_edge(eoe.get_id(), condition.PositiveInt())

        eoe.add_out_edge(eoe.get_id(), condition.TokenKind('SKIP'))
        eoe.add_out_edge(init.get_id(), condition.Operator())


if __name__ == '__main__':
    unittest.main()
