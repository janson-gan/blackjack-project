import random
from art import logo

# Define the deck of cards
# Ace is represented by 11, face (Jack, Queen, King) as 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deal 2 cards at the start of the game
def first_deal_card(hand):
    for _ in range(2):
        hand.append(random.choice(cards))

# Deal 1 card if ask for another card
def deal_card(hand):
     for _ in range(1):
        hand.append(random.choice(cards))

"""
Calculate the score of a hand
Adjust Aces from 11 to 1 if score exceeds 21
Detect Blackjack if 2 cards add up to 21
Return the score and is_blackjack result
"""
def cal_score(card):
    score = sum(card)
    ace = 11
    is_blackjack = score == 21 and len(card) == 2
    
    # Adjust Aces if score over 21
    while score > 21 and ace in card:
            card.remove(ace)
            card.append(1)
            score -= 10
    return score, is_blackjack

    
# === Game Loop ===
game_start = input("Do you want to play Blackjack game? Type 'y' for yes, and 'n' for no:\n").lower()

while game_start == "y":
    # Initialize fresh hands for this round
    print(logo)
    player_cards = []
    dealer_cards = []

    # Initial the deal
    first_deal_card(player_cards)
    first_deal_card(dealer_cards)

    # Calculate the initial score
    player_score, player_is_blackjack = cal_score(player_cards)
    dealer_score, dealer_is_blackjack = cal_score(dealer_cards)

    # check for Blackjack 
    if player_is_blackjack and dealer_is_blackjack:
        print(f"Both BlackJack! You lose!")
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")
    elif player_is_blackjack:
         print(f"You got a BlackJack! You win!")
         print(f"Your cards: {player_cards}, current score: {player_score}")
         print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")
    elif dealer_is_blackjack:
        print(f"Dealer BlackJack! You lose!")
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")

        # if no one blackjack, then game continue with cards on hand
    else:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer cards: {dealer_cards[0]}")
        get_card = input("Do you want to get another card? 'y' for yes, and 'n' for no:\n").lower()

        # Player turn
        while get_card == "y":
            deal_card(player_cards)
            player_score, player_is_blackjack = cal_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Dealer cards: {dealer_cards[0]}")

            # Player bust check
            if player_score > 21:
                    print(f"You busted! You lose!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
                    get_card = "n"
                    game_start = "n"
                    break
            else:
                get_card = input("Do you want to get another card? 'y' for yes, and 'n' for no:\n").lower()

        # Dealer turn
        if get_card == "n" and game_start == "y":
                while get_card == "n" and dealer_score < 17:
                    deal_card(dealer_cards)
                    dealer_score, dealer_is_blackjack = cal_score(dealer_cards)

                # Dealer bust check
                if dealer_score > 21:
                    print(f"Dealer busted! You win!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
                elif dealer_score > player_score:
                    print(f"You lose!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
                elif dealer_score < player_score:
                    print(f"You win!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
                else:
                    print(f"Is a tie!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
  
    # Replay prompt
    is_continue = input("Do you want to play again? 'y' for yes, 'n' for no:\n")
    if is_continue == "n":
        game_start = "n"
    elif is_continue == "y":
        game_start = "y"