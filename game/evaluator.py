from treys import Evaluator as TreysEvaluator, Card as TreysCard

class HandEvaluator:
    def __init__(self):
        self.evaluator = TreysEvaluator()

    def convert_to_treys(self, cards):
        treys_cards = []
        for card in cards:
            rank = card.rank
            suit = card.suit

            # mapping suits and ranks for treys
            suit_map = {'♠': 's', '♥': 'h', '♦': 'd', '♣': 'c'}
            rank_map = {'T': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A',
                        '9': '9', '8': '8', '7': '7', '6': '6', '5': '5',
                        '4': '4', '3': '3', '2': '2'}

            treys_str = rank_map[rank] + suit_map[suit]
            treys_cards.append(TreysCard.new(treys_str))
        return treys_cards

    def evaluate(self, hand_cards, community_cards):
        hand = self.convert_to_treys(hand_cards)
        board = self.convert_to_treys(community_cards)
        score = self.evaluator.evaluate(board, hand)
        return score  

    def get_rank_class(self, score):
        return self.evaluator.get_rank_class(score)

    def describe(self, score):
        return self.evaluator.class_to_string(self.get_rank_class(score))
