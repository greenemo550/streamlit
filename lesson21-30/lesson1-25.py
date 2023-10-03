class Dog:
    # コンストラクタ: オブジェクトを作成する際に呼び出される
    def __init__(self, name, age):
        self.name = name  # インスタンス変数
        self.age = age    # インスタンス変数

    # メソッド: オブジェクトの操作を定義
    def bark(self):
        print(f"{self.name} says Woof!")

    def get_age(self):
        return self.age

# オブジェクトの作成
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# オブジェクトのメソッドを呼び出す
dog1.bark()  # "Buddy says Woof!"を出力
print(dog2.get_age())  # 5を出力
