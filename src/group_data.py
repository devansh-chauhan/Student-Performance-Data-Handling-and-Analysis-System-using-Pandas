import os
import pandas as pd


def group_data(df):

    print("\n" + "=" * 60)
    print("DATA GROUPING")
    print("=" * 60)

    grouped = (
        df.groupby("Grade")
        .agg(
            Average_Marks=("Marks", "mean"),
            Student_Count=("Grade", "count"),
            Average_Attendance=("Attendance", "mean"),
        )
        .round(2)
    )

    print(grouped)

    os.makedirs("output", exist_ok=True)
    grouped.to_csv("output/grouped_report.csv")

    return df