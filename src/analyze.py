def analyze_data(df):

    print("\n" + "=" * 60)
    print("DATA ANALYSIS")
    print("=" * 60)

    total_students = len(df)

    average_marks = df["Marks"].mean()
    highest_marks = df["Marks"].max()
    lowest_marks = df["Marks"].min()

    average_attendance = df["Attendance"].mean()
    average_study_hours = df["StudyHours"].mean()

    passed_students = len(df[df["Result"] == "Pass"])
    failed_students = len(df[df["Result"] == "Fail"])

    pass_percentage = (passed_students / total_students) * 100
    fail_percentage = (failed_students / total_students) * 100

    grade_distribution = df["Grade"].value_counts()

    print(f"Total Students      : {total_students}")
    print(f"Average Marks       : {average_marks:.2f}")
    print(f"Highest Marks       : {highest_marks}")
    print(f"Lowest Marks        : {lowest_marks}")
    print(f"Average Attendance  : {average_attendance:.2f}")
    print(f"Average Study Hours : {average_study_hours:.2f}")
    print(f"Pass Percentage     : {pass_percentage:.2f}%")
    print(f"Fail Percentage     : {fail_percentage:.2f}%")

    print("\nGrade Distribution")
    print(grade_distribution)

    return df