def average(array):
    array = set(array)
    return round(sum(array) / len(array), 3)


number_heights = int(input())
heights = list(map(int, input().split()[:number_heights]))
result = average(heights)
print(result)