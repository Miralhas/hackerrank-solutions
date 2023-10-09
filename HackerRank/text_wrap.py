# full_string = ""
# new_list = []
# string = list(string)
# for i, char in enumerate(string):
#     full_string += char
#     if len(full_string) == max_width:
#         new_list.append(full_string)
#         full_string = ""
#     elif len(string) < max_width:
#         new_list.append(char)
#     # string.remove(char)

import textwrap

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

print(textwrap.fill(string, max_width))
