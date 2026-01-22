# Blackjack Game Project
## 🎲 Overview

This is a simple command-line Blackjack game implemented in Python. The project simulates a basic version of the popular card game where a player competes against the dealer.

## 📂 Project Structure

* **[task/main.py]: The main script containing the game logic.
* **[task/art.py]: Provides ASCII art (logo) for the game.

## 🃏 Game Rules Implemented

* Aces count as 11 but can be adjusted to 1 if the score exceeds 21.
* Blackjack is defined as a two-card hand totaling 21 (Ace + 10 (10, Jack, Queen, King)).
* Player can choose to hit (draw another card) or stand (end their turn).
* Dealer must draw cards until reaching a score of 17 or higher.
* Bust occurs if the score exceeds 21.
* Winner is determined by comparing scores if neither busts.
