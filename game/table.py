from game.card import Deck
from game.player import Player

class Table:
    def __init__(self, players):
        self.players = players  
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.current_stage = 'pre-flop'  

    def start_new_hand(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        self.current_stage = 'pre-flop'

        for player in self.players:
            player.reset_for_new_round()
            player.receive_cards(self.deck.deal(2))

    def deal_community_cards(self):
        if self.current_stage == 'pre-flop':
            self.community_cards = self.deck.deal(3)  # Flop
            self.current_stage = 'flop'
        elif self.current_stage == 'flop':
            self.community_cards += self.deck.deal(1)  # Turn
            self.current_stage = 'turn'
        elif self.current_stage == 'turn':
            self.community_cards += self.deck.deal(1)  # River
            self.current_stage = 'river'
        else:
            raise ValueError("All community cards already dealt.")

    def collect_bets(self):
        for player in self.players:
            self.pot += player.current_bet
            player.current_bet = 0

    def show_table_state(self):
        print(f"\n--- {self.current_stage.upper()} ---")
        print(f"Community cards: {self.community_cards}")
        print(f"Pot: {self.pot}")
        for p in self.players:
            print(p)
