from game.card import Deck
from game.table import Table
from game.evaluator import HandEvaluator
from game.round import BettingRound
from agents.rule_based import RuleBasedPlayer
from game.player import Player  

evaluator = HandEvaluator()
player1 = RuleBasedPlayer("Bot-Ali", evaluator)
player2 = RuleBasedPlayer("Bot-Sara", evaluator)
players = [player1, player2]
table = Table(players)

table.start_new_hand()
print("\n=== Pre-Flop ===")
table.show_table_state()

# Pre-Flop
BettingRound(players, table.community_cards, evaluator).take_turns()
table.collect_bets()

# Flop
table.deal_community_cards()
print("\n=== Flop ===")
table.show_table_state()
BettingRound(players, table.community_cards, evaluator).take_turns()
table.collect_bets()

# Turn
table.deal_community_cards()
print("\n=== Turn ===")
table.show_table_state()
BettingRound(players, table.community_cards, evaluator).take_turns()
table.collect_bets()

# River
table.deal_community_cards()
print("\n=== River ===")
table.show_table_state()
BettingRound(players, table.community_cards, evaluator).take_turns()
table.collect_bets()

active_players = [p for p in players if not p.folded]
if len(active_players) == 1:
    winner = active_players[0]
    print(f"\n🏆 {winner.name} wins by default! (Everyone else folded)")
else:
    results = []
    for p in active_players:
        score = evaluator.evaluate(p.hand, table.community_cards)
        desc = evaluator.describe(score)
        results.append((score, p, desc))
        print(f"{p.name}: {p.hand} → {desc} (score = {score})")

    results.sort(key=lambda x: x[0])
    best_score, winner, hand_type = results[0]
    print("\n🎉 Winner:", winner.name)
    print("🃏 Hand Type:", hand_type)
    print("💰 Pot:", table.pot)
