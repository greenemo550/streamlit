def add_element(my_list, element):
    # この部分を完成させてください
    my_list.append(element)
    return my_list

def remove_element(my_list, element):
    # この部分を完成させてください
    my_list.remove(element)
    return my_list

def sort_list(my_list):
    # この部分を完成させてください
    my_list.sort()
    return my_list

def find_element(my_list, element):
    # この部分を完成させてください
    return my_list.index(element)
    
def pop_last_element(my_list):
    # この部分を完成させてください
    return my_list.pop(-1)  

def reverse_list(my_list):
    # この部分を完成させてください
    my_list.reverse()
    return my_list

test_list = [5, 2, 9, 1, 5, 6]

print(add_element(test_list, 10))  # 期待する出力: [5, 2, 9, 1, 5, 6, 10]
print(remove_element(test_list, 9))  # 期待する出力: [5, 2, 1, 5, 6, 10]
print(sort_list(test_list))  # 期待する出力: [1, 2, 5, 5, 6, 10]
print(find_element(test_list, 5))  # 期待する出力: 2 (最初に見つかった5の位置)
print(pop_last_element(test_list))  # 期待する出力: 10 (最後の要素を取り出す)
print(reverse_list(test_list))  # 期待する出力: [6, 5, 5, 2, 1]
