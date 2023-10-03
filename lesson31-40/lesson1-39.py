import pandas as pd

student_data = {
    'Student ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Anna', 'Ben', 'Charlie', 'Diana', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack'],
    'Math Score': [85, 78, 92, 65, 88, 76, 95, 80, 85, 74],
    'Science Score': [90, 77, 89, 68, 80, 76, 93, 88, 85, 78],
    'History Score': [88, 82, 91, 65, 87, 70, 96, 85, 82, 75]
}
df = pd.DataFrame(student_data)

ass = df[df["Math Score"] >= 80]["Science Score"].mean()
print(ass)

subjects = {"Math Score", "Science Score", "History Score"}

for subject in subjects:
    min_score = df[subject].min()
    student_name = df[df[subject] == min_score]["Name"].values[0]
    print(f"The student with the lowest {subject} is {student_name} with a score of {min_score}")

df["Average Score"] = df[["Math Score", "Science Score", "History Score"]].mean(axis=1)
top_student = df[df["Average Score"] == df["Average Score"].max()]
print(top_student["Name"].values[0])
