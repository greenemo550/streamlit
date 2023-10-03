#問題1-2: 文字列のリストの逆順 reverse
def reverse_strings(fruits):
    fruits.reverse()
    return fruits
    
fruits = ["apple", "banana", "cherry"]
reversed_fruits = reverse_strings(fruits)
print(reversed_fruits)