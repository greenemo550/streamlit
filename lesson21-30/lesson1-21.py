def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

def count_lines(filename):
    with open(filename, "r") as file:
        lines = file.read().split("\n")
        if lines[-1] == "":
            lines.pop()
        line_count = len(lines)
        return line_count

write_to_file("sample1.txt", "apple")
print(read_from_file("sample1.txt"))
print(count_lines("sample1.txt"))



