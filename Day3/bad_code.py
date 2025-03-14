import numpy as np
import random

'''
READABLE
REUSABLE
UNDERSTANDABLE
TESTABLE
'''

num_players = 7

random.seed(42)
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck_list = [f'{number} of {suit}' for suit in suits for number in numbers]
random.shuffle(deck_list)

def deal_cards(deck_list, num_players, debug=False):
    assert num_players*5 <= 52, "Too many players, not enough cards!"

    # Create handout list - {'1': [], '2': []... 'num_players': []}
    handout = {f'{i+1}': [] for i in range(num_players)}

    for player in handout:
        for _ in range(5):
            card = deck_list.pop()
            handout[player].append(card) # add it to plays hand
        # hand = np.random.choice(deck_list, 5, replace=False)
    
    if debug:
        for player, hand in handout.items():
            print(f"{player}'s hand: {hand}")
    
    return handout


def test_dealing(deal_cards):
    # Test 1: Check num_players were dealt cards
    assert len(deal_cards(deck_list, num_players=0)) == 0, "Cards were dealt to no one!"
    assert len(deal_cards(deck_list, num_players=1)) == 1, "Cards were not dealt to player!"
    assert len(deal_cards(deck_list, num_players=7)) == 7, "Cards were not dealt to all players!"

    # Test 2: Check if maximum number of players is followed
    try:
        deal_cards(deck_list, num_players=100) 
    except AssertionError:
        print('Too many players detected (test passed)')


test_dealing(deal_cards)