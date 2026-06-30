#  Student Performance Data Handling and Analysis System using Pandas

A Python-based data analysis project that demonstrates the complete data processing lifecycle using the **Pandas** library. This project loads, cleans, transforms, analyzes, and generates reports from a student performance dataset.

---

##  Project Overview

Educational institutions collect large amounts of student data such as study hours, attendance, and examination marks. Raw datasets often contain missing values, duplicate records, and inconsistencies that make analysis difficult.

This project automates the complete data handling process by:

* Loading student data from a CSV file
* Inspecting and cleaning the dataset
* Transforming the data by creating new features
* Filtering and sorting records
* Performing statistical analysis
* Generating summary reports
* Exporting processed datasets as CSV files

---

##  Features

### Module 1 – Data Loading

* Read CSV file using Pandas
* Display first and last five records
* Display dataset shape
* Display column names
* Display data types

### Module 2 – Data Inspection

* Detect missing values
* Detect duplicate records
* Display descriptive statistics
* Display dataset information
* Check memory usage

### Module 3 – Data Cleaning

* Remove duplicate records
* Handle missing values
* Remove unnecessary columns
* Validate attendance values
* Validate study hours
* Validate marks
* Export cleaned dataset

### Module 4 – Data Transformation

* Assign Grades
* Determine Pass/Fail status
* Calculate Performance Score

### Module 5 – Data Filtering

* Top-performing students
* Failed students
* Students with attendance below 75%
* Students studying more than 8 hours

### Module 6 – Data Analysis

* Average marks
* Highest marks
* Lowest marks
* Average attendance
* Average study hours
* Pass percentage
* Fail percentage
* Grade distribution

### Module 7 – Data Sorting

* Sort by marks
* Sort by attendance
* Sort by study hours

### Module 8 – Data Grouping

* Average marks by grade
* Student count by grade
* Average attendance by grade

### Module 9 – Statistical Analysis

* Mean
* Median
* Mode
* Standard deviation
* Variance
* Correlation matrix

### Module 10 – Report Generation

* Generate summary report
* Export report as CSV

---

##  Technologies Used

* Python 3
* Pandas
* Matplotlib *(Optional Bonus)*
* OpenPyXL *(Optional Excel Export)*
* Git
* GitHub

---

##  Project Structure

```text
Student-Performance-Data-Handling-and-Analysis-System-using-Pandas/
│
├── data/
│   └── student_dataset_v2.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── toppers.csv
│   ├── failed_students.csv
│   ├── low_attendance.csv
│   ├── high_study_hours.csv
│   ├── sorted_by_marks.csv
│   ├── sorted_by_attendance.csv
│   ├── sorted_by_study_hours.csv
│   ├── grouped_report.csv
│   ├── correlation_matrix.csv
│   ├── grade_distribution.csv
│   └── attendance_distribution.png
│   └── marks_histogram.png
│   └── performance_score.png
│   └── grade_distribution.png
│   └── report.csv
│
├── src/
│   ├── load_data.py
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── transform.py
│   ├── filter_data.py
│   ├── analyze.py
│   ├── sort_data.py
│   ├── group_data.py
│   ├── statistics.py
|   ├── menu.py
|   ├── visualization.py
│   └── report.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/devansh-chauhan/Student-Performance-Data-Handling-and-Analysis-System-using-Pandas.git
```

Move into the project directory:

```bash
cd Student-Performance-Data-Handling-and-Analysis-System-using-Pandas
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

##  Running the Project

Execute:

```bash
python main.py
```

---

##  Output Files

The program generates the following files inside the `output` folder:

* cleaned_data.csv
* toppers.csv
* failed_students.csv
* low_attendance.csv
* high_study_hours.csv
* sorted_by_marks.csv
* sorted_by_attendance.csv
* sorted_by_study_hours.csv
* grouped_report.csv
* correlation_matrix.csv
* grade_distribution.csv
* report.csv

---

##  Skills Demonstrated

* Data Cleaning
* Data Preprocessing
* Data Transformation
* Data Filtering
* Statistical Analysis
* Data Aggregation
* Report Generation
* CSV File Handling
* Modular Python Programming
* Version Control using Git & GitHub

---

##  Learning Outcomes

This project helped strengthen practical knowledge of:

* Python Programming
* Pandas Library
* Data Analysis
* Data Cleaning Techniques
* File Handling
* Modular Code Design
* Git and GitHub Workflow

---

##  Author

**Devansh Chauhan**

GitHub: https://github.com/devansh-chauhan

---

##  License

This project was developed for educational purposes as part of a Python and Pandas coursework assignment.
