from game.player import Player
from game.evaluator import HandEvaluator

class RuleBasedPlayer(Player):
    def __init__(self, name, evaluator, stack=1000):
        super().__init__(name, stack)
        self.evaluator = evaluator

    def decide(self, community_cards, current_bet):
        if self.folded:
            return 'fold', 0

        total_cards = self.hand + community_cards
        can_call = (current_bet - self.current_bet) <= self.stack
        can_raise = (current_bet - self.current_bet + 50) <= self.stack

        # 🟢 Pre-Flop strategy
        if len(total_cards) < 5:
            strong_hands = ['A', 'K', 'Q', 'J']
            high_card = self.hand[0].rank in strong_hands or self.hand[1].rank in strong_hands
            if high_card and can_raise:
                return 'raise', 50
            elif can_call and self.current_bet < current_bet:
                return 'call', current_bet - self.current_bet
            else:
                return 'check', 0

        # 🟢 Post-Flop strategy
        score = self.evaluator.evaluate(self.hand, community_cards)
        if score < 300 and can_raise:
            return 'raise', 50
        elif score < 700:
            if can_call and self.current_bet < current_bet:
                return 'call', current_bet - self.current_bet
            else:
                return 'check', 0
        else:
            if self.current_bet < current_bet:
                return 'fold', 0
            else:
                return 'check', 0
