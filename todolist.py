class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, index):
        if index < 0 or index >= len(self.tasks):
            print("無効なインデックスです。")
            return
        del self.tasks[index]

    def display_tasks(self):
        if not self.tasks:
            print("タスクはありません")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def main():
        todo_list = ToDoList()

        while True:
            print("\n--- ToDoリスト ---")
            todo_list.display_tasks()
            print("1. タスクを追加")
            print("2. タスクを削除")
            print("3. 終了")

            choice = input("> ")

            if choice == "1":
                task = input("追加するタスクを入力してください: ")
                todo_list.add_task(task)
            
            elif choice == "2":
                index = int(input("削除するタスクの番号を入力してください: "))
                todo_list.remove_task(index)
            
            elif choice == "3":
                print("終了します")
                break
            else:
                print("無効な選択です。再度選択してください。")
    
if __name__ == "__main__":
    main()
