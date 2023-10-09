'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0
HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()

# for char in x:
#     lower.append(char)
#     upper.append(char.upper())

def swap_cases(input_string):
    output_string = ""
    for char in input_string:
        if char in upper:
            output_string += char.lower()
        elif char in lower:
            output_string += char.upper()
        else:
            output_string += char
    
    return output_string

def swapcases2(string):
    newstr=str()

    for letter in string:
        if letter.islower():
            newstr += letter.upper()
        else:
            newstr += letter.lower()
        # else:
        #     newstr += letter

    return newstr

print(swap_cases("Victor."))
print(swapcases2("Victor."))
