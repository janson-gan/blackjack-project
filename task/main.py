# Game setting:
# playing cards stored in a list as below:
# [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# the four 10s represent 10, jack, queen and king
# Ace represented by 11
# if two cards add up to 21 and contain 11 and 10, consider bkackjack
# 1. Game start with player and dealer handed with two random cards
# 2. Check for blackjack (ace + 10) 
# Challenges: to detect player and dealer cards are blackjack (11, 10)
# how to continue the game if both user or dealer get a blackjack
# the new game keep started after player busted, forgotten to add game_start = n
# use thonny to check the iteration of the while loop to figure out player adding card till busted logic

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def first_deal_card(to_who):
    for _ in range(2):
        to_who.append(random.choice(cards))

def deal_card(to_who):
     for _ in range(1):
        to_who.append(random.choice(cards))

def cal_score(card):
    score = sum(card)
    ace = 11
    is_blackjack = score == 21 and len(card) == 2
    while score > 21 and ace in card:
            card.remove(ace)
            card.append(1)
            score -= 10
    return score, is_blackjack

    

game_start = input("Do you want to play Blackjack game? Type 'y' for yes, and 'n' for no:\n").lower()

while game_start == "y":
    # Initialize fresh hands for this round
    print(logo)
    player_cards = []
    dealer_cards = []
    first_deal_card(player_cards)
    first_deal_card(dealer_cards)
    player_score, player_is_blackjack = cal_score(player_cards)
    dealer_score, dealer_is_blackjack = cal_score(dealer_cards)
    # check player, dealer or both for blackjack. if either blackjack, game end  
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

        while get_card == "y":
            deal_card(player_cards)
            player_score, player_is_blackjack = cal_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Dealer cards: {dealer_cards[0]}")
            if player_score > 21:
                    print(f"You busted! You lose!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
                    get_card = "n"
                    game_start = "n"
                    break
            else:
                get_card = input("Do you want to get another card? 'y' for yes, and 'n' for no:\n").lower()

        if get_card == "n" and game_start == "y":
                while get_card == "n" and dealer_score < 17:
                    deal_card(dealer_cards)
                    dealer_score, dealer_is_blackjack = cal_score(dealer_cards)
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
                    print(f"Is a tie! You lose!")
                    print(f"Your final cards: {player_cards}, final score: {player_score}")
                    print(f"Dealer cards: {dealer_cards}, final score: {dealer_score}")
  
    is_continue = input("Do you want to play again? 'y' for yes, 'n' for no:\n")
    if is_continue == "n":
        game_start = "n"
    elif is_continue == "y":
        game_start = "y"