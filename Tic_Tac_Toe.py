'''
!pip install ttkthemes
!pip install time
'''
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import time

class TicTacToe:
    def _init_(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Applying themed style
        self.style = ThemedStyle(self.window)
        self.style.set_theme("arc")
        self.style.configure('Game.TButton', font=('Helvetica', 20))  # Setting font for buttons
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ttk.Button(
                    self.window, 
                    text="", 
                    width=8,
                    style='Game.TButton',  # Applying custom style
                    command=lambda i=i, j=j: self.make_move(i, j)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")
            self.animate_button(self.buttons[row][col])  # Animate button after click
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False
    
    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    
    def animate_button(self, button):
        button.configure(style='Game.TButton')
        self.window.update()
        time.sleep(0.05)
        button.configure(style='TButton')

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()