# Student Performance Analysis Using Python

## Project Overview
This project analyzes how study habits and academic activities relate to exam performance. It uses a **self-created synthetic dataset** containing 500 fictional student records. No real student information is used.

## Objectives
- Explore and clean data using Pandas.
- Calculate statistical measures using NumPy.
- Perform descriptive and group-based analysis.
- Explore correlations between numeric variables.
- Create visualizations using Matplotlib.
- Export a summary report to CSV.

## Dataset
`data/student_performance.csv` contains 500 rows and 10 columns.

| Column | Description |
|---|---|
| student_id | Unique fictional student ID |
| age | Student age |
| gender | Female, Male or Other |
| study_hours_per_day | Average daily study hours |
| attendance_percentage | Attendance percentage |
| sleep_hours_per_day | Average daily sleep hours |
| assignment_score | Assignment score out of 100 |
| extracurricular_participation | Yes/No participation |
| exam_score | Exam score out of 100 |
| performance_category | Needs Improvement, Good or Excellent |

The dataset is generated with a fixed random seed, so the same dataset can be reproduced.

## Tools and Libraries
- Python
- NumPy
- Pandas
- Matplotlib

## Folder Structure
```text
student_performance_analysis/
├── data/
│   └── student_performance.csv
├── outputs/
│   └── Charts and performance_summary.csv (generated after running)
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run the Project in VS Code

1. Extract the ZIP file.
2. Open the `student_performance_analysis` folder in VS Code.
3. Select **Terminal → New Terminal**.
4. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the project:

   ```bash
   python main.py
   ```

The terminal displays the dataset overview, statistical measures, group comparisons and correlations. The `outputs` folder will contain four charts and `performance_summary.csv`.

## Analysis Performed
1. Dataset shape, first records, data types and missing-value check.
2. Duplicate removal and numeric missing-value handling.
3. NumPy mean, median, standard deviation, minimum and maximum.
4. Pandas descriptive statistics and group-by analysis.
5. Correlation analysis.
6. Matplotlib visualizations:
   - Exam score distribution
   - Study hours vs exam score
   - Exam scores by performance category
   - Correlation heatmap

## Questions Explored
- How do study hours relate to exam scores?
- How does attendance relate to exam performance?
- How do average scores differ across performance categories?
- Which numeric variables have the strongest correlation with exam score?

## Note
This is an educational project using synthetic data. Correlation does not prove causation, and the results should not be generalized to real students.

## Author
Replace this line with your name before LMS submission.
