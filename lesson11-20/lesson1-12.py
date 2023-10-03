with open("sample.txt", "r") as file:
    content = file.read()

lines = content.split("\n")
#最後の行が空なら削除
if lines[-1] == "":
    lines.pop()
line_count = len(lines)

words = content.split()
word_count = len(words)

character_count = len(content)

print(line_count)
print(word_count)
print(character_count)
