flags = {
    "alphanumeric": False,
    "alphabetical": False,
    "digits": False,
    "lower_case": False,
    "upper_case": False
    }

user_string = input()

for char in user_string:
    if char.isalnum():
        flags["alphanumeric"] = True
    if char.isalpha():
        flags["alphabetical"] = True
    if char.isdigit():
        flags["digits"] = True
    if char.islower():
        flags["lower_case"] = True
    if char.isupper():
        flags["upper_case"] = True

for values in flags.values():
    print(values)