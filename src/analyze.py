import os

def filter_data(df):

    print("\n" + "=" * 60)
    print("DATA FILTERING")
    print("=" * 60)

    os.makedirs("output", exist_ok = True)

    toppers = df[df["Grade"] == "A"]
    toppers.to_csv("output/toppers.csv", index = False)

    failed_students = df[df["Result"] == "Fail"]
    failed_students.to_csv("output/failed_students.csv", index = False)

    low_attendance = df[df["Attendance"] < 75]
    low_attendance.to_csv("output/low_attendance.csv", index=False)

    high_study_hours = df[df["StudyHours"] > 8]
    high_study_hours.to_csv("output/high_study_hours.csv", index=False)

    print(f"Top Performers: {len(toppers)}")
    print(f"Failed Students: {len(failed_students)}")
    print(f"Attendance < 75%: {len(low_attendance)}")
    print(f"Study Hours > 8: {len(high_study_hours)}")

    return df