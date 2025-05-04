class Player:
    def __init__(self, name, stack=1000):
        self.name = name
        self.stack = stack       
        self.hand = []          
        self.current_bet = 0     
        self.folded = False      

    def receive_cards(self, cards):
        self.hand = cards

    def bet(self, amount):
        if amount > self.stack:
            raise ValueError(f"{self.name} doesn't have enough chips.")
        self.stack -= amount
        self.current_bet += amount
        return amount

    def fold(self):
        self.folded = True

    def reset_for_new_round(self):
        self.hand = []
        self.current_bet = 0
        self.folded = False

    def __repr__(self):
        status = "Folded" if self.folded else "Active"
        return f"{self.name} | Chips: {self.stack} | Hand: {self.hand} | {status}"
