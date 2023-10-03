#add_entry: 辞書にキーと値を追加して、辞書全体を返す。
def add_entry(my_dict, key, value):
    # この部分を完成させてください
    my_dict[key] = value
    return my_dict

#get_value: 指定されたキーの値を返す。キーが存在しない場合は、"Not found"を返す。
def get_value(my_dict, key):
    # この部分を完成させてください
    return my_dict.get(key, "Not found")
     
#get_keys: 辞書の全てのキーをリストとして返す。
def get_keys(my_dict):
    # この部分を完成させてください
    return list(my_dict.keys())

#update_dict: 別の辞書とマージして、更新された辞書全体を返す。
def update_dict(my_dict, another_dict):
    # この部分を完成させてください
    my_dict.update(another_dict)
    return my_dict

# テスト
test_dict = {"apple": 5, "banana": 8, "cherry": 12}
print(add_entry(test_dict, "date", 7))  # 期待する出力: {"apple": 5, "banana": 8, "cherry": 12, "date": 7}
print(get_value(test_dict, "banana"))  # 期待する出力: 8
print(get_value(test_dict, "mango"))  # 期待する出力: "Not found"
print(get_keys(test_dict))  # 期待する出力: ["apple", "banana", "cherry", "date"]
print(update_dict(test_dict, {"fig": 3, "grape": 15}))  # 期待する出力: {"apple": 5, "banana": 8, "cherry": 12, "date": 7, "fig": 3, "grape": 15}
