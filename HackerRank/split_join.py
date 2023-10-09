def split_and_join(line):
    letter = line.split()
    letter = "-".join(letter)

    return letter

line = input()
result = split_and_join(line)
print(result)