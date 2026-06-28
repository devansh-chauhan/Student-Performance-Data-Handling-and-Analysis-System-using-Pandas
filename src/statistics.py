import os

def statistical_analysis(df):
    print("\n" + "=" * 60)
    print("STATISTICAL ANALYSIS")
    print("=" * 60)

    stats = {
        "Mean Marks": df["Marks"].mean(),
        "Median Marks": df["Marks"].median(),
        "Mode Marks": df["Marks"].mode()[0],
        "Standard Deviation": df["Marks"].std(),
        "Varience": df["Marks"].var(),
    }

    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")

    print("\nCorrelation Matrix:")
    correlation = df[["StudyHours", "Attendance", "Marks"]].corr()
    print(correlation)

    os.makedirs("output", exist_ok = True)
    correlation.to_csv("output/correlation_matrix.csv")

    return df