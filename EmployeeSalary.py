import numpy as np
import pandas as pd

salary = np.array([
    [25000, 2, 80],
    [45000, 5, 90],
    [30000, 3, 75],
    [60000, 8, 95],
    [35000, 4, 85]
])

# 1. Average salary
avg_salary = np.mean(salary[:, 0])
print("1. Average Salary:", avg_salary)

# 2. Highest salary
highest_salary = np.max(salary[:, 0])
print("2. Highest Salary:", highest_salary)

# 3. Lowest salary
lowest_salary = np.min(salary[:, 0])
print("3. Lowest Salary:", lowest_salary)

# 4. Average experience
avg_experience = np.mean(salary[:, 1])
print("4. Average Experience:", avg_experience)

# 5. Salary greater than 40000
employees_salary = np.where(salary[:, 0] > 40000)[0] + 1
print("5. Salary > 40000:", employees_salary)

employees_performance = np.where(salary[:, 2] > 80)[0] + 1
print("6. Performance > 80:", employees_performance)

highest_performance = np.argmax(salary[:, 2]) + 1
print("7. Highest Performance Employee:", highest_performance)

salary_std = np.std(salary[:, 0])
print("8. Salary Standard Deviation:", salary_std)

salary_class = np.where(
    salary[:, 0] >= 40000,
    "High Salary",
    "Low Salary"
)
print("9. Salary Classification:", salary_class)

# 10. DataFrame
df = pd.DataFrame(
    salary,
    columns=["Salary", "Experience", "Performance"]
)

df["Salary Class"] = salary_class

print("\n10. Final DataFrame:")
print(df)