def get_score(students, name):
    return students.get(name, "Not found")

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
}
  
print(get_score(students, "Alice"))