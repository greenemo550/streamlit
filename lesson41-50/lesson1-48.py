import pandas as pd

students = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'Subject': ['English', 'Mathematics', 'Science', 'English', 'Mathematics'],
    'Marks': [90, 85, 88, 78, 80]
})

average_score = students.groupby("Subject")["Marks"].mean()
print(average_score)

students["Range"] = students["Marks"] - students["Marks"].min()
print(students["Range"])

high_marks_students = students[students["Marks"] >= 85]
print(high_marks_students)
