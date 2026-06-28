from src.load_data import load_data
from src.inspect_data import inspect_data
from src.clean_data import clean_data
from src.transform import transform_data
from src.filter_data import filter_data
from src.analyze import analyze_data
from src.sort_data import sort_data
from src.group_data import group_data
from src.statistics import statistical_analysis
from src.report import generate_report
from src.visualization import generate_charts

DATASET_PATH = "data/student_dataset_v2.csv"


def menu():

    df = None

    while True:

        print("\n" + "=" * 50)
        print(" STUDENT PERFORMANCE DATA HANDLING AND ANALYSIS SYSTEM ")
        print("=" * 50)

        print("\n1. Load Data")
        print("2. Inspect Data")
        print("3. Clean Data")
        print("4. Transform Data")
        print("5. Analyze Data")
        print("6. Generate Report")
        print("7. Generate Charts")
        print("8. Run Complete Project")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            df = load_data(DATASET_PATH)

        elif choice == "2":
            if df is None:
                print("Please load the dataset first (Option 1).")
            else:
                inspect_data(df)

        elif choice == "3":
            if df is None:
                print("Please load the dataset first (Option 1).")
            else:
                df = clean_data(df)

        elif choice == "4":
            if df is None:
                print("Please load the dataset first (Option 1).")
            else:
                df = transform_data(df)

        elif choice == "5":
            if df is None:
                print("Please load the dataset first (Option 1).")
            else:
                filter_data(df)
                analyze_data(df)
                sort_data(df)
                group_data(df)
                statistical_analysis(df)

        elif choice == "6":
            if df is None:
                print("Please load the dataset first (Option 1).")
            else:
                generate_report(df)

        elif choice == "7":
            if df is None:
                print("Please load the dataset first (Option 1).")
            else:
                generate_charts(df)

        elif choice == "8":
            df = load_data(DATASET_PATH)
            inspect_data(df)
            df = clean_data(df)
            df = transform_data(df)
            filter_data(df)
            analyze_data(df)
            sort_data(df)
            group_data(df)
            statistical_analysis(df)
            generate_report(df)
            generate_charts(df)

        elif choice == "9":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")