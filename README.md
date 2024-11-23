## Tic-Tac-Toe RL Agent - A Comprehensive Reinforcement Learning Project

This README provides an overview of the Tic-Tac-Toe RL Agent project, covering data processing, environment creation, agent implementation, evaluation, and a Streamlit deployment for an interactive game.

### **Data Processing:**

- The script loads a CSV dataset (expected to be in the `data` folder) containing Tic-Tac-Toe board configurations and corresponding outcomes.
- It assigns descriptive names to the columns and encodes categorical values (x, o, b) into numerical representations (1, -1, 0).
- The data is then split into features (`X`) and target (`y`) variables.

### **Environment Creation:**

- The `TicTacToeEnv` class defines the environment for playing Tic-Tac-Toe.
- It initializes a 3x3 board and keeps track of the game state (done, winner).
- The `step` method takes an action (index representing a cell) and player (1 or -1) as input and updates the board, rewards, and game state.
- The `check_winner` method checks for winning conditions (rows, columns, diagonals).

### **Agent Implementation:**

- The `QLearningAgent` class implements the Q-Learning algorithm for learning optimal Tic-Tac-Toe strategies.
- It maintains a Q-table that stores estimated Q-values for each state-action pair.
- The `get_q_value` method retrieves the Q-value from the table.
- The `update_q_value` method updates the Q-value based on the Bellman equation, considering reward, next state, and exploration.
- The `select_action` method employs an epsilon-greedy strategy to balance exploration (random actions) and exploitation (choosing the action with the highest Q-value).

### **Evaluation:**

- The `random_opponent` function generates random valid moves for an opponent.
- The `evaluate_agent` function plays multiple games against a specified opponent (random or rule-based) and tracks wins, losses, and draws.

### **Deployment (Streamlit App):**

- The script utilizes Streamlit to create a web app for playing Tic-Tac-Toe against the RL Agent.
- It defines a simplified `TicTacToeEnv` class tailored for the Streamlit interface.
- A `RandomAgent` is used for demonstration purposes (replace it with your trained Q-Learning agent for actual gameplay).
- The app displays the game board, allows players to select moves, and showcases the agent's move selection.
- It also checks for winning conditions and displays appropriate messages.

### **Further Enhancements:**

- Implement a more sophisticated rule-based opponent for a greater challenge.
- Introduce different difficulty levels for the opponent.
- Integrate logging features to analyze the agent's learning process.
- Visualize the game board and Q-value updates for better understanding.
- Experiment with hyperparameter tuning for the agent to optimize its performance.

This project provides a solid foundation for building and deploying a Tic-Tac-Toe RL agent using Q-Learning. With further development and exploration, you can create a more challenging and engaging Tic-Tac-Toe experience using reinforcement learning.