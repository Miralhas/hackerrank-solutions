def mutate_string(string, postiion, character):

    l = list(string)
    l[position] = character
    string = "".join(l)

    return string

input_string = input()
position, character = input().split()
position = int(position)
x = mutate_string(input_string, position, character)
