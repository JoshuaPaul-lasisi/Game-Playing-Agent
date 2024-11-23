# q_learning_agent.py
import random
import numpy as np

class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=1.0, epsilon_decay=0.99):
        self.q_table = {}
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay

    def get_q_value(self, state, action):
        return self.q_table.get((tuple(state.flatten()), action), 0)

    def update_q_value(self, state, action, reward, next_state):
        max_next_q = max([self.get_q_value(next_state, a) for a in range(9)])
        current_q = self.get_q_value(state, action)
        self.q_table[(tuple(state.flatten()), action)] = current_q + self.lr * (reward + self.gamma * max_next_q - current_q)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 8)
        q_values = [self.get_q_value(state, a) for a in range(9)]
        return np.argmax(q_values)

# Call the QLearning agent creation when this script is executed
if __name__ == "__main__":
    agent = QLearningAgent()
    print("Agent created with epsilon:", agent.epsilon)