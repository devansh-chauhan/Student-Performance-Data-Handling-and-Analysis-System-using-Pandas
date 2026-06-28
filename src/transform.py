import os

def assign_grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
def assign_result(marks):
    return "Pass" if marks >= 40 else "Fail"

def calculate_performance_score(row):
    return round(
        (row["Marks"] * 0.6)
        + (row["Attendance"] * 0.3)
        + (row["StudyHours"] * 0.1),
        2,
    )

def transform_data(df):
    
    print("\n" + "=" * 60)
    print("DATA TRANSFORMATION")
    print("=" * 60)

    df["Grade"] = df["Marks"].apply(assign_grade)

    df["Result"] = df["Marks"].apply(assign_result)

    df["PerformanceScore"] = df.apply(
        calculate_performance_score,
        axis=1,
    )

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_data.csv", index=False)

    print("Transformation completed successfully.")

    return df