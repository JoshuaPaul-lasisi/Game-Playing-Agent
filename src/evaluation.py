import random
import numpy as np
from tic_tac_toe_env import TicTacToeEnv
from q_learning_agent import QLearningAgent

def random_opponent(board):
    """Random opponent selects a random valid action."""
    valid_actions = [i for i in range(9) if board.flatten()[i] == 0]
    return random.choice(valid_actions) if valid_actions else None

def rule_based_opponent(board):
    """Simple rule-based opponent (example: blocks or wins if possible)."""
    # Example: Check for winning or blocking moves, otherwise choose random
    for i in range(9):
        if board.flatten()[i] == 0:  # Check empty space
            # Dummy rule: the opponent just blocks or wins (very simple strategy)
            return i
    return random_opponent(board)  # Default to random if no winning or blocking move

def evaluate_agent(agent, env, num_games=100, opponent="random"):
    results = {"wins": 0, "losses": 0, "draws": 0}
    for _ in range(num_games):
        state = env.reset()
        done = False
        player_turn = 1  # Agent starts first

        while not done:
            if player_turn == 1:  # Agent's turn
                action = agent.select_action(state)
            else:  # Opponent's turn
                if opponent == "random":
                    action = random_opponent(state)
                elif opponent == "rule":
                    action = rule_based_opponent(state)  # Rule-based opponent logic

            if action is None:  # No valid moves, game over
                break

            _, reward, done = env.step(action, player_turn)
            player_turn *= -1  # Alternate turns

        # Record results
        if env.winner == 1:
            results["wins"] += 1
        elif env.winner == -1:
            results["losses"] += 1
        else:
            results["draws"] += 1

    print(f"Evaluation Results: {results}")
    return results

# If this script is executed directly, you can evaluate the agent
if __name__ == "__main__":
    # Setup the environment and agent
    env = TicTacToeEnv()
    agent = QLearningAgent()

    # Run evaluation against a random opponent
    evaluate_agent(agent, env, num_games=100, opponent="random")