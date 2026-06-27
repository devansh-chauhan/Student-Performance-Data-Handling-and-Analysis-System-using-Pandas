import pandas as pd

def inspect_data(df):
    print("\n" + "=" * 60)
    print("DATA INSPECTION")
    print("=" * 60)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nDescriptive Statistics:")
    print(df.describe(include="all"))

    print("\nMemory Usage:")
    print(df.memory_usage(deep=True))

    print("\nDataset Information:")
    df.info()

    