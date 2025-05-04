from game.card import Deck
from game.player import Player
from game.table import Table
from game.evaluator import HandEvaluator

player1 = Player("Ali")
player2 = Player("Sara")
table = Table([player1, player2])
evaluator = HandEvaluator()

table.start_new_hand()

print("\n=== Pre-Flop ===")
table.show_table_state()

table.deal_community_cards()
print("\n=== Flop ===")
table.show_table_state()

# Turn
table.deal_community_cards()
print("\n=== Turn ===")
table.show_table_state()

# River
table.deal_community_cards()
print("\n=== River ===")
table.show_table_state()

results = []
for p in table.players:
    score = evaluator.evaluate(p.hand, table.community_cards)
    desc = evaluator.describe(score)
    results.append((score, p, desc))
    print(f"{p.name}: {p.hand} → {desc} (score = {score})")

results.sort(key=lambda x: x[0])
best_score, winner, hand_type = results[0]

print("\n🎉 Winner:", winner.name)
print("🃏 Hand Type:", hand_type)
