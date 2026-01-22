# Blackjack Game Project
## 🎲 Overview

This is a simple command-line Blackjack game implemented in Python. The project simulates a basic version of the popular card game where a player competes against the dealer.

## 📂 Project Structure

* **[task/main.py](https://github.com/janson-gan/blackjack-project/tree/main/task): The main script containing the game logic.
* **[task/art.py](https://github.com/janson-gan/blackjack-project/tree/main/task): Provides ASCII art (logo) for the game.

## 🃏 Game Rules Implemented

* Aces count as 11 but can be adjusted to 1 if the score exceeds 21.
* Blackjack is defined as a two-card hand totaling 21 (Ace + 10 (10, Jack, Queen, King)).
* Player can choose to hit (draw another card) or stand (end their turn).
* Dealer must draw cards until reaching a score of 17 or higher.
* Bust occurs if the score exceeds 21.
* Winner is determined by comparing scores if neither busts.

## ⚙️ How It Works

1. **Initial Deal**: Both player and dealer receive two cards.
2. **Blackjack Check**: If either has Blackjack, the game ends immediately.
3. **Player Turn**: Player decides whether to hit or stand.
4. **Dealer Turn**: Dealer draws until reaching at least 17.
5. **Result**: Scores are compared to determine the winner.

## 🧩 Key Functions

* `first_deal_card(hand)`: Deals two cards to the given hand.
* `deal_card(hand)`: Deals one card to the given hand.
* `cal_score(card)`: Calculates the score of a hand, adjusting Aces as needed.

## 🚀 How to Run

1. Ensure you have Python installed.
2. Run the game with:
   ```bash
   python main.py
3. Follow the on-screen prompt to play.

## ⚠️ Challenges
1. Detecting player and dealer cards as Blackjack (Ace and 10 value card)
   - Solution: Implement a function to check if the initial two cards contain an Ace (11) and a 10 value card and flag it as Blackjack.
2. Handling game continuation if both player and dealer get Blackjack.
   - Solution: Add logic to detect simultaneous Blackjacks and decide the outcome (e.g. tie) before proceeding.
3. Game keep restarting after player busts(forgot to add ```game_start = 'n'```)
   - Solution: Ensure the game state variable ```game_start``` is reset after a bust to allow a new game to start cleanly.
4. Too many indentation due to ```while loop``` and ```if-else``` statement causing confusion.
   - Solution: Use [thonny](https://thonny.org/) debugging tool to monitor loop iterations and validate the logic accordingly.

