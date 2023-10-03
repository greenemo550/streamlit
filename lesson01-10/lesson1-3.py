#問題 1-3: 辞書を利用したデータの管理
def get_job_by_name(people, name):
    for person in people:
        if person["name"] == name:
            return name + ": " + person["job"]
    return "Not found"


people = [
    {'name': 'Alice', 'age': 28, 'job': 'Engineer'},
    {'name': 'Bob', 'age': 22, 'job': 'Student'},
    {'name': 'Charlie', 'age': 35, 'job': 'Doctor'},
]

name = input("名前を入力してください")

print(get_job_by_name(people, name))