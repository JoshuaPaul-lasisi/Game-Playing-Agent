import streamlit as st
import numpy as np
import random
from tic_tac_toe_env import TicTacToeEnv
from q_learning_agent import RandomAgent

# Streamlit App
st.title("Tic-Tac-Toe RL Agent")

# Tic-Tac-Toe Environment Class (Simplified)
class TicTacToeEnv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0 = empty, 1 = X, -1 = O
        self.winner = None

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.winner = None
        return self.board

    def step(self, action, player):
        row, col = divmod(action, 3)
        if self.board[row, col] != 0:
            return self.board, -10, True  # Invalid move (penalty)

        self.board[row, col] = player
        done, winner = self.check_win()
        if done:
            self.winner = winner
            return self.board, 1 if winner == 1 else -1, done  # 1 for X win, -1 for O win
        return self.board, 0, done  # No win yet

    def check_win(self):
        for i in range(3):
            if abs(np.sum(self.board[i, :])) == 3:  # Check rows
                return True, np.sign(np.sum(self.board[i, :]))
            if abs(np.sum(self.board[:, i])) == 3:  # Check columns
                return True, np.sign(np.sum(self.board[:, i]))
        if abs(np.sum(np.diag(self.board))) == 3:  # Check diagonals
            return True, np.sign(np.sum(np.diag(self.board)))
        if abs(np.sum(np.diag(np.fliplr(self.board)))) == 3:
            return True, np.sign(np.sum(np.diag(np.fliplr(self.board))))
        if np.count_nonzero(self.board) == 9:  # Draw condition
            return True, 0
        return False, None

# Define your RL agent here (simplified example)
class RandomAgent:
    def select_action(self, board):
        valid_actions = [i for i in range(9) if board.flatten()[i] == 0]
        return random.choice(valid_actions) if valid_actions else None

# Initialize Environment and Agent
env = TicTacToeEnv()
agent = RandomAgent()  # Use your trained agent here if you have one

if "state" not in st.session_state:
    st.session_state["state"] = env.reset()
    st.session_state["done"] = False

# Display Board
def display_board(board):
    symbols = {1: "X", -1: "O", 0: " "}
    board_display = [[symbols[cell] for cell in row] for row in board]
    for row in board_display:
        st.write("|".join(row))
        st.write("-" * 5)

st.header("Tic-Tac-Toe Board")
display_board(st.session_state["state"])

# Player Move
if not st.session_state["done"]:
    st.write("Your Turn! Select a square:")
    col1, col2, col3 = st.columns(3)
    actions = {}
    for i, col in enumerate([col1, col2, col3]):
        for j in range(3):
            idx = i * 3 + j
            row, col_pos = divmod(idx, 3)
            if st.session_state["state"][row, col_pos] == 0:
                if col.button(f"Place at {idx+1}"):
                    _, _, done = env.step(idx, -1)  # Player is "O"
                    st.session_state["done"] = done

# Agent Move
if not st.session_state["done"]:
    agent_action = agent.select_action(st.session_state["state"])
    _, _, st.session_state["done"] = env.step(agent_action, 1)  # Agent is "X"
    st.session_state["state"] = env.board

if st.session_state["done"]:
    if env.winner == 1:
        st.write("Agent Wins!")
    elif env.winner == -1:
        st.write("You Win!")
    else:
        st.write("It's a Draw!")