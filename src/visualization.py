import os
import matplotlib.pyplot as plt

def generate_charts(df):

    os.makedirs("output", exist_ok=True)

    plt.figure(figsize=(6, 4))
    df["Grade"].value_counts().sort_index().plot(kind="bar")
    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("output/grade_distribution.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(6, 4))
    plt.hist(df["Marks"], bins=10)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("output/marks_histogram.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(6, 4))
    plt.hist(df["Attendance"], bins=10)
    plt.title("Attendance Distribution")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Students")
    plt.tight_layout()
    plt.savefig("output/attendance_distribution.png")
    plt.show()
    plt.close()

    plt.figure(figsize=(6, 4))
    plt.plot(df["PerformanceScore"])
    plt.title("Performance Score")
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("output/performance_score.png")
    plt.show()
    plt.close()

    print("\nCharts generated successfully.")