import tkinter as tk
from tkinter import messagebox
import random

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Pro - Python Edition")
        self.root.geometry("700x550")
        self.root.configure(bg="#1b3d2f") # Dark green casino-style background

        # Deck setup with suits
        self.suits = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
        self.deck = []
        self.reset_deck()

        self.player_hand = []
        self.dealer_hand = []
        
        self.setup_ui()
        self.start_new_game()

    def reset_deck(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [(v, s) for v in values for s in self.suits]
        random.shuffle(self.deck)

    def setup_ui(self):
        # Dealer Frame
        tk.Label(self.root, text="DEALER", font=("Helvetica", 14, "bold"), bg="#1b3d2f", fg="white").pack(pady=10)
        self.dealer_frame = tk.Frame(self.root, bg="#1b3d2f")
        self.dealer_frame.pack(pady=10)

        # Center result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"), bg="#1b3d2f", fg="#f1c40f")
        self.result_label.pack(pady=20)

        # Player Frame
        self.player_frame = tk.Frame(self.root, bg="#1b3d2f")
        self.player_frame.pack(pady=10)
        tk.Label(self.root, text="PLAYER", font=("Helvetica", 14, "bold"), bg="#1b3d2f", fg="white").pack(pady=5)
        
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 12), bg="#1b3d2f", fg="#bdc3c7")
        self.score_label.pack()

        # Buttons
        self.btn_frame = tk.Frame(self.root, bg="#1b3d2f")
        self.btn_frame.pack(side="bottom", pady=30)

        self.btn_hit = tk.Button(self.btn_frame, text="HIT", command=self.hit, width=15, height=2, bg="#27ae60", fg="white", font=("Arial", 10, "bold"))
        self.btn_hit.grid(row=0, column=0, padx=10)

        self.btn_stand = tk.Button(self.btn_frame, text="STAND", command=self.stand, width=15, height=2, bg="#c0392b", fg="white", font=("Arial", 10, "bold"))
        self.btn_stand.grid(row=0, column=1, padx=10)

    def draw_card(self, parent, card_data, hidden=False):
        """Draws an elegant card with colored borders and suits."""
        bg_color = "white" if not hidden else "#2c3e50"
        
        card_frame = tk.Frame(parent, bg=bg_color, highlightbackground="#000", highlightthickness=2, width=80, height=120)
        card_frame.pack_propagate(False)
        card_frame.pack(side="left", padx=8)

        if hidden:
            tk.Label(card_frame, text="?", font=("Arial", 24), bg=bg_color, fg="white").place(relx=0.5, rely=0.5, anchor="center")
        else:
            val, suit = card_data
            symbol = self.suits[suit]
            color = "#e74c3c" if suit in ['Hearts', 'Diamonds'] else "black"
            
            # Value top-left
            tk.Label(card_frame, text=val, font=("Arial", 12, "bold"), bg="white", fg=color).place(x=5, y=5)
            # Center symbol
            tk.Label(card_frame, text=symbol, font=("Arial", 30), bg="white", fg=color).place(relx=0.5, rely=0.5, anchor="center")
            # Value bottom-right
            tk.Label(card_frame, text=val, font=("Arial", 12, "bold"), bg="white", fg=color).place(x=55, y=95)

    def start_new_game(self):
        if len(self.deck) < 10: self.reset_deck()
        self.result_label.config(text="")
        self.btn_hit.config(state="normal")
        self.btn_stand.config(state="normal")
        
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.update_ui()

    def update_ui(self, reveal_dealer=False):
        for w in self.player_frame.winfo_children(): w.destroy()
        for w in self.dealer_frame.winfo_children(): w.destroy()

        for card in self.player_hand:
            self.draw_card(self.player_frame, card)

        for i, card in enumerate(self.dealer_hand):
            if i == 1 and not reveal_dealer:
                self.draw_card(self.dealer_frame, card, hidden=True)
            else:
                self.draw_card(self.dealer_frame, card)

        score = self.get_score(self.player_hand)
        self.score_label.config(text=f"Score: {score}")

    def get_score(self, hand):
        score = 0
        aces = 0
        for val, suit in hand:
            if val in ['J', 'Q', 'K']: score += 10
            elif val == 'A': score += 11; aces += 1
            else: score += int(val)
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def hit(self):
        self.player_hand.append(self.deck.pop())
        self.update_ui()
        if self.get_score(self.player_hand) > 21:
            self.end_game("BUST! YOU LOST.")

    def stand(self):
        self.btn_hit.config(state="disabled")
        self.btn_stand.config(state="disabled")
        
        while self.get_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
            
        self.update_ui(reveal_dealer=True)
        p_score = self.get_score(self.player_hand)
        d_score = self.get_score(self.dealer_hand)

        if d_score > 21: self.end_game("DEALER BUSTS! YOU WIN!")
        elif p_score > d_score: self.end_game("YOU WIN!")
        elif p_score < d_score: self.end_game("DEALER WINS.")
        else: self.end_game("PUSH (DRAW)")

    def end_game(self, message):
        self.result_label.config(text=message)
        self.btn_hit.config(state="disabled")
        self.btn_stand.config(state="disabled")
        self.root.after(2000, self.start_new_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()