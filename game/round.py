class BettingRound:
    def __init__(self, players, community_cards, evaluator):
        self.players = [p for p in players if not p.folded]
        self.active_players = self.players[:]
        self.current_bet = 0
        self.community_cards = community_cards
        self.evaluator = evaluator

    def take_turns(self):
        while True:
            everyone_called = True
            for player in self.active_players:
                if player.folded:
                    continue

                if hasattr(player, 'decide'):
                    action, amount = player.decide(self.community_cards, self.current_bet)
                    print(f"\n🤖 {player.name} decides to {action} ({amount})")
                else:
                    print(f"\n🧑 {player.name}'s turn | Stack: {player.stack} | Current bet: {self.current_bet}")
                    print(f"Hand: {player.hand}")
                    action = input(f"{player.name}, choose action (fold/check/call/raise): ").strip().lower()
                    amount = 0
                    if action == 'raise':
                        amount = int(input("Enter raise amount: "))

                if action == 'fold':
                    player.fold()
                elif action == 'check':
                    if player.current_bet != self.current_bet:
                        print("❌ Cannot check, must call or fold.")
                        return self.take_turns()
                elif action == 'call':
                    diff = self.current_bet - player.current_bet
                    player.bet(diff)
                elif action == 'raise':
                    total_bet = self.current_bet + amount
                    diff = total_bet - player.current_bet
                    player.bet(diff)
                    self.current_bet = total_bet
                    everyone_called = False
                else:
                    print("❌ Invalid action.")
                    return self.take_turns()

            if everyone_called:
                break

        print("\n✅ Betting round finished.")
