import numpy as np
import pandas as pd

dataset = np.array([[12000, 15000, 18000],
                   [10000, 14000, 16000],
                   [18000, 20000, 22000],
                   [9000, 12000, 15000],
                   [15000, 17000, 19000]])

sales = dataset

months = ["January", "February", "March"]

total_sales = np.sum(sales, axis=1)
print("1. Total Sales:", total_sales)
average_sales = np.mean(sales, axis=1)
print("2. Average Sales:", average_sales)
highest_monthly = np.max(sales, axis=0)
print("3. Highest Monthly Sales:", highest_monthly)
lowest_monthly = np.min(sales, axis=0)
print("4. Lowest Monthly Sales:", lowest_monthly)
best_salesperson = np.argmax(total_sales) + 1
print("5. Best Salesperson:", best_salesperson)
above_15000 = np.where(average_sales > 15000)[0] + 1
print("6. Salespersons above 15000:", above_15000)
company_sales = np.sum(sales, axis=0)
print("7. Company Monthly Sales:", company_sales)
std_sales = np.std(sales, axis=0)
print("8. Standard Deviation:", std_sales)
classification = np.where(
    average_sales >= 18000,
    "Excellent",
    np.where(
        average_sales >= 14000,
        "Good",
        "Needs Improvement"
    )
)
print("9. Classification:", classification)
df = pd.DataFrame(sales, columns=months)
df["Total Sales"] = total_sales
df["Average Sales"] = average_sales
df["Classification"] = classification
print("\n10. Final DataFrame:")
print(df)