import streamlit as st
import numpy as np
import random
from tic_tac_toe_env import TicTacToeEnv
from q_learning_agent import QLearningAgent

# Streamlit App
st.title("Tic-Tac-Toe RL Agent")

# Initialize Environment and Agent
env = TicTacToeEnv()
agent = QLearningAgent()  # Use your trained agent here if you have one

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