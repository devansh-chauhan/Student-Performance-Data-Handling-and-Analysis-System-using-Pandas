import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)

        print("=" * 60)
        print("STUDENT PERFORMANCE DATASET")
        print("=" * 60)

        print("\nFirst 5 Records:")
        print(df.head())

        print("\nLast 5 Records:")
        print(df.tail())

        print("\nShape of Dataset:")
        print(df.shape)

        print("\nColumn Names:")
        print(df.columns)

        print("\nData types:")
        print(df.dtypes)

        return df

    except FileNotFoundError:
        print("Error: Dataset not found.")
        return None
    
    except Exception as e:
        print("An error occurred:", e)
        return None