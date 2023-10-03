def average_score(students):
    average = sum(students.values()) / len(students)
    return average

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

print(average_score(students))