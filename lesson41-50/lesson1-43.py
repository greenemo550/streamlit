import pandas as pd

employee_data = {
    'Name': ['Anna', 'Ben', 'Charlie', 'Diana', 'Eva', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'Finance', 'Engineering', 'HR', 'Engineering', 'Finance', 'Finance', 'Engineering'],
    'Join Year': [2019, 2018, 2020, 2019, 2020, 2017, 2018, 2019],
    'Salary': [70000, 80000, 120000, 75000, 115000, 82000, 79000, 125000]
}

df = pd.DataFrame(employee_data)

average_salary = df[df["Join Year"] == 2020]["Salary"].mean()
print(average_salary)

deprtment_group = df.groupby("Department").size()
print(deprtment_group)

high_salary = df[df["Salary"] >= 80000]
print(high_salary[["Name", "Department"]])

high_salary_employees = df[df["Salary"] == df["Salary"].max()]
print(high_salary_employees[["Name", "Salary"]])