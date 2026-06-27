import os
import pandas as pd

def clean_data(df):
    print("\n" + "=" * 60)
    print("DATA CLEANING")
    print("=" * 60)

    unnamed_columns = [col for col in df.columns if col.startswith("Unnamed")]
    if unnamed_columns:
        df = df.drop(columns = unnamed_columns)
        print(f"Removed columns: {unnamed_columns}")
    
    duplicates = df.duplicated().sum()
    if duplicates:
        df = df.drop_duplicates()
    print(f"Duplicate records removed: {duplicates}")

    missing_before = df.isnull().sum().sum()
    df = df.dropna()
    print(f"Missing values removed: {missing_before}")

    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

    df = df[df["StudyHours"] >=0]

    df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

    os.makedirs("output", exist_ok = True)

    output_file = "output/cleaned_data.csv"
    df.to_csv(output_file, index = False)

    print(f"Cleaned dataset saved to: {output_file}")

    return df