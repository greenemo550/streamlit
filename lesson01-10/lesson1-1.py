#問題1-2: 文字列のリストの逆順　スライス
def reverse_strings(fruits):
    reversed_fruits = fruits[: : -1]
    return reversed_fruits

fruits = ["apple", "banana", "cherry"]

print(reverse_strings(fruits))