# data_processing.py
import pandas as pd

def process_data():
    # Load and process data
    data = pd.read_csv("../data/tic-tac-toe.data", header=None)
    data.columns = [
        "top-left", "top-middle", "top-right",
        "middle-left", "middle-middle", "middle-right",
        "bottom-left", "bottom-middle", "bottom-right",
        "outcome"
    ]

    mapping = {'x': 1, 'o': -1, 'b': 0, 'positive': 1, 'negative': 0}
    data = data.replace(mapping).infer_objects(copy=False)

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    print("Processed data:")
    print(X[:5], y[:5])

# Call the function when this script is executed
if __name__ == "__main__":
    process_data()