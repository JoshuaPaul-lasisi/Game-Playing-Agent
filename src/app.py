import streamlit as st
import numpy as np
from q_learning_agent import QLearningAgent
from tic_tac_toe_env import TicTacToeEnv

# Streamlit App
st.title("Tic-Tac-Toe RL Agent")

# Initialize Environment and Agent
env = TicTacToeEnv()
agent = QLearningAgent()  # Use your trained agent here if you have one

# Initialize game state in Streamlit session state
if "state" not in st.session_state:
    st.session_state["state"] = env.reset()
    st.session_state["done"] = False
    st.session_state["invalid_move"] = False  # Track invalid moves

# Display Board
def display_board(board, disabled_buttons):
    symbols = {1: "X", -1: "O", 0: " "}
    board_display = [[symbols[cell] for cell in row] for row in board]
    
    # Create columns once
    cols = st.columns(3)  # Create the columns outside the loop
    
    for i, row in enumerate(board_display):
        for j, cell in enumerate(row):
            idx = i * 3 + j
            unique_key = f"{i}-{j}-{idx}-{str(np.random.randint(1000000))}"  # Ensure unique key
            disabled = disabled_buttons[idx] or st.session_state["done"]
            if cols[j].button(f"{cell}", key=unique_key, disabled=disabled):
                return idx  # Return the index of the button clicked
    return None

# Player Move
def player_move():
    invalid_move = False
    disabled_buttons = [False] * 9
    action = None

    if st.session_state["done"]:
        return None, disabled_buttons
    
    st.write("Your Turn! Select a square:")

    # Check for player move
    action = display_board(st.session_state["state"], disabled_buttons)
    if action is not None:
        row, col = divmod(action, 3)
        _, reward, done = env.step(action, -1)  # Player is "O"
        st.session_state["done"] = done
        if reward == -10:  # Invalid move penalty
            invalid_move = True
        disabled_buttons[action] = True  # Disable button after it's pressed
    
    return invalid_move, disabled_buttons

# Agent Move
def agent_move():
    if not st.session_state["done"]:
        agent_action = agent.select_action(st.session_state["state"])
        _, _, st.session_state["done"] = env.step(agent_action, 1)  # Agent is "X"
        st.session_state["state"] = env.board

# Display winner message
def display_winner():
    if st.session_state["done"]:
        if env.winner == 1:
            st.write("Agent Wins!")
        elif env.winner == -1:
            st.write("You Win!")
        else:
            st.write("It's a Draw!")

# Main game loop
invalid_move, disabled_buttons = player_move()

# If the player made an invalid move, show a message
if invalid_move:
    st.error("Invalid move! Please choose a different spot.")

# Perform agent's move
if not st.session_state["done"]:
    agent_move()

# Display the board again with the current state
st.header("Tic-Tac-Toe Board")
display_board(st.session_state["state"], disabled_buttons)

# Display the winner
display_winner()