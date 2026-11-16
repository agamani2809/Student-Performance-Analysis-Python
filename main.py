from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "student_performance.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA_PATH)
    print("\\n========== DATASET OVERVIEW ==========")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    print("\\nFirst five records:\\n", df.head())
    print("\\nData types:\\n", df.dtypes)
    print("\\nMissing values:\\n", df.isnull().sum())

    df = df.drop_duplicates()
    numeric_cols = df.select_dtypes(include=np.number).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    scores = df["exam_score"].to_numpy()
    print("\\n========== NUMPY STATISTICS ==========")
    print(f"Mean: {np.mean(scores):.2f}")
    print(f"Median: {np.median(scores):.2f}")
    print(f"Standard deviation: {np.std(scores):.2f}")
    print(f"Maximum: {np.max(scores):.1f} | Minimum: {np.min(scores):.1f}")

    print("\\n========== PANDAS ANALYSIS ==========")
    print(df.describe().round(2))
    print("\\nAverage score by gender:\\n",
          df.groupby("gender")["exam_score"].mean().round(2))
    print("\\nAverage score by category:\\n",
          df.groupby("performance_category")["exam_score"].mean().round(2))
    print("\\nCorrelation with exam score:\\n",
          df.select_dtypes(include=np.number).corr()["exam_score"].sort_values(ascending=False).round(2))
    summary = df.groupby("performance_category").agg(
        student_count=("student_id", "count"),
        average_exam_score=("exam_score", "mean"),
        average_study_hours=("study_hours_per_day", "mean"),
        average_attendance=("attendance_percentage", "mean")
    ).round(2)
    summary.to_csv(OUTPUT_DIR / "performance_summary.csv")

    # 1. Exam score distribution
    plt.figure(figsize=(8,5))
    plt.hist(df["exam_score"], bins=20, edgecolor="black")
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam score"); plt.ylabel("Number of students")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR/"exam_score_distribution.png", dpi=150); plt.close()

    # 2. Study hours vs exam score
    plt.figure(figsize=(8,5))
    for category, group in df.groupby("performance_category"):
        plt.scatter(group["study_hours_per_day"], group["exam_score"], label=category, alpha=.65)
    plt.title("Study Hours vs Exam Score")
    plt.xlabel("Study hours per day"); plt.ylabel("Exam score")
    plt.legend(); plt.tight_layout()
    plt.savefig(OUTPUT_DIR/"study_hours_vs_score.png", dpi=150); plt.close()

    # 3. Score distribution by category
    categories = ["Needs Improvement", "Good", "Excellent"]
    box_data = [df.loc[df["performance_category"]==c, "exam_score"] for c in categories]
    plt.figure(figsize=(8,5))
    plt.boxplot(box_data, tick_labels=categories)
    plt.title("Exam Scores by Performance Category")
    plt.xlabel("Performance category"); plt.ylabel("Exam score")
    plt.xticks(rotation=10); plt.tight_layout()
    plt.savefig(OUTPUT_DIR/"scores_by_category.png", dpi=150); plt.close()

    # 4. Correlation heatmap using Matplotlib
    corr = df.select_dtypes(include=np.number).corr()
    plt.figure(figsize=(9,6))
    image = plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(image, label="Correlation")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.columns)), corr.columns)
    for i in range(len(corr)):
        for j in range(len(corr)):
            plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", fontsize=8)
    plt.title("Correlation Heatmap")
    plt.tight_layout(); plt.savefig(OUTPUT_DIR/"correlation_heatmap.png", dpi=150); plt.close()

    print(f"\\nDone! Charts and summary saved in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
