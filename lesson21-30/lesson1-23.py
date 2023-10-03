# 1. 提供された関数をコピー

def last_element(t):
    return t[-1]

def swap_keys_values(d):
    return {value: key for key, value in d.items()}

def key_exists(d, key):
    return key in d

def keys_as_tuple(d):
    return tuple(d.keys())

# 2. サンプルデータの作成
sample_tuple = (1, 2, 3, 4, 5)
sample_dict = {"apple": 1, "banana": 2, "cherry": 3}

# 3. 各関数を実行して結果を出力
print(last_element(sample_tuple))  # 期待する出力: 5
print(swap_keys_values(sample_dict))  # 期待する出力: {1: 'apple', 2: 'banana', 3: 'cherry'}
print(key_exists(sample_dict, "apple"))  # 期待する出力: True
print(key_exists(sample_dict, "mango"))  # 期待する出力: False
print(keys_as_tuple(sample_dict))  # 期待する出力: ('apple', 'banana', 'cherry')
