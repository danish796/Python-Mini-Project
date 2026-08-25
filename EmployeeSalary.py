import numpy as np
import pandas as pd
salary = np.array([[25000, 2, 80], [45000, 5, 90], [30000, 3, 75], [60000, 8, 95], [35000, 4, 85]])
columns = ['Salary', 'Experience', 'Performance']
total_salary = np.sum(salary, axis=1)
average_salary = np.mean(salary, axis=1)
average_salary = np.array(average_salary, dtype=int)
highest_salary = np.max(salary, axis=1)
lowest_salary = np.min(salary, axis=1)
above_40000 = np.sum(salary > 40000, axis=1)
employee_performance = salary[:, 2]
status = np.where(average_salary > 40000, "Eligible for Promotion", "Not Eligible for Promotion")
index = np.arange(1, len(salary) + 1)
std_subject = np.std(salary, axis=0)
df = pd.DataFrame(salary, columns=columns)
df['total_salary'] = total_salary 
df['average_salary'] = average_salary
df['highest_salary'] = highest_salary
df['lowest_salary'] = lowest_salary
df['employee_performance'] = employee_performance
df['above_40000'] = above_40000
df['status'] = status
print(df)
