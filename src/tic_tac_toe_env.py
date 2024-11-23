# tic_tac_toe_env.py
import numpy as np

class TicTacToeEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
        return self.board

    def step(self, action, player):
        row, col = divmod(action, 3)
        if self.board[row, col] != 0:
            return self.board, -10, True
        self.board[row, col] = player
        if self.check_winner(player):
            self.done = True
            self.winner = player
            return self.board, 1 if player == 1 else -1, True
        if not np.any(self.board == 0):
            self.done = True
            self.winner = 0
            return self.board, 0, True
        return self.board, 0, False

    def check_winner(self, player):
        for row in self.board:
            if np.all(row == player):
                return True
        for col in self.board.T:
            if np.all(col == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

# Call the environment creation when this script is executed
if __name__ == "__main__":
    env = TicTacToeEnv()
    print("Environment reset:", env.reset())