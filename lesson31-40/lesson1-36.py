import pandas as pd

employees_data = {
    'Employee ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'Finance', 'Engineering', 'HR', 'Finance', 'Engineering', 'Engineering', 'HR'],
    'Salary': [60000, 65000, 70000, 62000, 66000, 71000, 72000, 63000],
    'Joining Year': [2019, 2019, 2018, 2020, 2020, 2018, 2019, 2020]
}

df = pd.DataFrame(employees_data)

average_salary = df[df["Department"] == "Engineering"]["Salary"].mean()
print(average_salary)

year_group = len(df[df["Joining Year"] == 2020])
print(year_group)

top_salary = df[df["Salary"] == df["Salary"].max()]
print(top_salary["Name"].values[0], top_salary["Salary"].values[0])

department_group = df.groupby("Department")["Salary"].mean()
print(department_group)

sort = df[df["Joining Year"] == 2019].sort_values(by = "Salary", ascending=False)
print(sort)