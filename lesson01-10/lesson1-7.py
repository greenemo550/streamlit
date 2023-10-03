def average_score(students):
    return sum(students.values()) / len(students)

def above_average_score(students):
    average = average_score(students)  # ここでaverage_score関数を再利用
    return [student for student, score in students.items() if score >= average]

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

print(above_average_score(students))
