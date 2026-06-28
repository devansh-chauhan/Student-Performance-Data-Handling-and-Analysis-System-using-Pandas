import os

def sort_data(df):
    print("\n" + "=" * 60)
    print("DATA SORTING")
    print("=" * 60)

    os.makedirs("output", exist_ok = True)

    marks_sorted = df.sort_values(by="Marks", ascending=False)
    marks_sorted.to_csv("output/sorted_by_marks.csv", index=False)

    attendance_sorted = df.sort_values(by="Attendance", ascending=False)
    attendance_sorted.to_csv("output/sorted_by_attendance.csv", index=False)

    study_hours_sorted = df.sort_values(by="StudyHours", ascending=False)
    study_hours_sorted.to_csv("output/sorted_by_study_hours.csv", index=False)

    print("\nTop 5 Students by Marks:")
    print(marks_sorted.head())

    print("\nTop 5 Students by Attendance:")
    print(attendance_sorted.head())

    print("\nTop 5 Students by Study Hours:")
    print(study_hours_sorted.head())

    return df