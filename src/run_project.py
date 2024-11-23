# run_project.py

import os
import sys
import importlib

# Function to run scripts in sequence
def run_script(script_name):
    try:
        # Importing the script as a module
        module = importlib.import_module(script_name)
        print(f"Running {script_name}...")
    except ModuleNotFoundError:
        print(f"Error: {script_name} not found.")
        sys.exit(1)

# Paths of scripts to run in sequence
scripts = [
    "data_processing",
    "tic_tac_toe_env",
    "q_learning_agent",
    "evaluation"
]

# Execute each script in sequence
for script in scripts:
    run_script(script)

print("All scripts executed successfully.")