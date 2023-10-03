#問題1-1: リストの中の重複を除去して、新しいリストを作成する。
def remove_duplicates(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


input_list = [1, 2, 2, 3, 4, 4, 4, 5]

print(remove_duplicates(input_list))
