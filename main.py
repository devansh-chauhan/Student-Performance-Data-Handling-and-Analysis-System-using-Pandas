from src.load_data import load_data
from src.inspect_data import inspect_data
from src.clean_data import clean_data
from src.transform import transform_data
from src.filter_data import filter_data
from src.analyze import analyze_data
from src.sort_data import sort_data
from src.group_data import group_data
from src.statistics import statistical_analysis

DATASET_PATH = "data/student_dataset_v2.csv"

def main():
    df = load_data(DATASET_PATH)

    if df is not None:
        print("\nData loaded successfully!!!")
        inspect_data(df)
        df = clean_data(df)
        df = transform_data(df)
        df = filter_data(df)
        df = analyze_data(df)
        df = sort_data(df)
        df = group_data(df)
        df = statistical_analysis(df)

if __name__ == "__main__":
    main()