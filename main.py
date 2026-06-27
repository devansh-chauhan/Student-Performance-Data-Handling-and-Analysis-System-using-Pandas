from src.load_data import load_data
from src.inspect_data import inspect_data

DATASET_PATH = "data/student_dataset_v2.csv"

def main():
    df = load_data(DATASET_PATH)

    if df is not None:
        # print("\nData loaded successfully!!!")
        inspect_data(df)

if __name__ == "__main__":
    main()