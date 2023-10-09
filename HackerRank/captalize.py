def solve(words):
    full_name = ""
    words = words.split(" ")
    for word in words:
        full_name += f"{word.capitalize()} "

    return full_name.strip()

words = input()
print(solve(words))