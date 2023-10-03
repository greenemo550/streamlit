def highest_score(students):
    max_score = max(students.values())
    for student, score in students.items():
        if score == max_score:
            return student

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

print(highest_score(students))