def reverse_my_dict(my_dict):
    return {v: k for k, v in my_dict.items()} 

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(reverse_my_dict(my_dict))
