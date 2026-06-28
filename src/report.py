import os
import pandas as pd

def generate_report(df):

    print("\n" + "=" * 60)
    print("REPORT GENERATION")
    print("=" * 60)

    report = {
        "Total Students": [len(df)],
        "Passed Students": [len(df[df["Result"] == "Pass"])],
        "Failed Students": [len(df[df["Result"] == "Fail"])],
        "Highest Marks": [df["Marks"].max()],
        "Lowest Marks": [df["Marks"].min()],
        "Average Marks": [round(df["Marks"].mean(), 2)],
        "Average Attendance": [round(df["Attendance"].mean(), 2)],
    }

    report_df = pd.DataFrame(report)
    print(report_df)

    grade_distribution = (
        df["Grade"]
        .value_counts()
        .rename_axis("Grade")
        .reset_index(name="Count")
    )

    print("\nGrade Distribution:")
    print(grade_distribution)

    os.makedirs("output", exist_ok=True)

    report_df.to_csv("output/report.csv", index=False)
    grade_distribution.to_csv("output/grade_distribution.csv", index=False)

    print("\nReport saved successfully.")

    return report_df