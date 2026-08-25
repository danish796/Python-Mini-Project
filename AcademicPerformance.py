import pandas as pd
import matplotlib.pyplot as plt

# Dataset
dataset = [
    [75, 80, 85],
    [80, 75, 60],
    [78, 50, 55]
]

columns = ["P", "C", "M"]
students = ["Student 1", "Student 2", "Student 3"]


df = pd.DataFrame(dataset, columns=columns)
# Calculations
total_marks = df.sum(axis=1)
average_marks = total_marks / len(columns)
percentage = (total_marks / 300) * 100
highest_marks = df.max(axis=0)
lowest_marks = df.min(axis=0)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].bar(students, average_marks)
axes[0, 0].set_title("Average Marks")
axes[0, 0].set_xlabel("Students")
axes[0, 0].set_ylabel("Average Marks")
axes[0, 1].bar(students, percentage)
axes[0, 1].set_title("Percentage")
axes[0, 1].set_xlabel("Students")
axes[0, 1].set_ylabel("Percentage (%)")
axes[1, 0].bar(columns, highest_marks)
axes[1, 0].set_title("Highest Marks by Subject")
axes[1, 0].set_xlabel("Subjects")
axes[1, 0].set_ylabel("Marks")
axes[1, 1].bar(columns, lowest_marks)
axes[1, 1].set_title("Lowest Marks by Subject")
axes[1, 1].set_xlabel("Subjects")
axes[1, 1].set_ylabel("Marks")
fig.suptitle("Academic Performance Dashboard", fontsize=16)
plt.tight_layout()
# Display
plt.show()