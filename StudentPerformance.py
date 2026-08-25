import numpy as np
import pandas as pd
marks = np.array([[85, 80, 90], [70, 75, 65], [92, 88, 95], [60, 72, 68], [78, 82, 80]])
columns = ['Math', 'Science', 'English']
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)
average_marks = np.array(average_marks, dtype=int)
highest_score = np.max(marks, axis=1)
lowest_score = np.min(marks, axis=1)
above_80 = np.sum(marks > 80, axis=1)
status = np.where(average_marks >= 75, "Pass", "Fail")
index = np.arange(1, len(marks) + 1)
std_subject = np.std(marks, axis=0)
df = pd.DataFrame(marks, columns=columns)
df['total_marks'] = total_marks
df['average_marks'] = average_marks
df['highest_score'] = highest_score
df['lowest_score'] = lowest_score
df['above_80'] = above_80
df['status'] = status
print(df)

