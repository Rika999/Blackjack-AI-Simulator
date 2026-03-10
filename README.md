# Blackjack

Author: Federica Di Dio

This project implements a complete Blackjack simulator developed entirely in Python. The application features a native graphical user interface (GUI), game logic based on standard casino rules, and a dynamic scoring engine.

The software is designed to be completely standalone, requiring no external libraries or external image assets, ensuring maximum portability and ease of execution.

## Technical Features

* **Graphical User Interface (GUI)**: Developed using the standard Tkinter library.
* **Procedural Rendering**: Cards are generated dynamically via code, including chromatic handling of suits (Red for Hearts and Diamonds, Black for Spades and Clubs).
* **Dynamic Ace Logic**: An algorithm that optimizes the value of the Ace (1 or 11) to prevent the player from busting.
* **Dealer AI**: A deterministic engine based on the "Stand on Soft 17" rule.
* **State Management**: Contextual disabling of controls during gameplay phases to prevent input errors.



## Project Architecture

The code follows Object-Oriented Programming (OOP) principles to ensure maintainability and scalability.

### Deck Management
The deck is initialized as a list of tuples `(value, suit)`. The `random.shuffle()` function is utilized to ensure unpredictability and fair gameplay.

### Scoring Engine
The scoring calculation follows an iterative cycle:
1. Summation of nominal card values.
2. Identification of Aces in the hand.
3. If the total exceeds 21, the value of each Ace is reduced from 11 to 1 until the total is within legal limits or no more Aces remain to be adjusted.

### Graphical Card Rendering
Each card is composed of Tkinter widgets:
* **Frame**: Defines the card rectangle and borders.
* **Labels**: Display the alphanumeric value (2-10, J, Q, K, A).
* **Unicode Symbols**: Uses `♠, ♥, ♦, ♣` to represent suits, eliminating dependencies on external image files.



## Game Logic

1. **Dealing**: Two cards are assigned to the player and two to the dealer (with one card face-down).
2. **Player Turn**: The user can choose to `HIT` (request a card) or `STAND` (end turn).
3. **Dealer Turn**: The dealer automatically draws cards until their total score is at least 17.
4. **Outcome Verification**:
    * If the player busts (> 21): Immediate loss.
    * If the dealer busts (> 21): Player victory.
    * Final Comparison: The highest score wins; ties result in a "Push" (draw).

## Requirements

* **Python 3.x**
* Standard libraries: `tkinter`, `random` (no external dependencies required).

## Usage

Clone the repository and run the main script:

```bash
python blackjack_ia.py
