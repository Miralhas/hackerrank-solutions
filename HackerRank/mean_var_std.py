import numpy

old_array = []
lines, cols = input().split()

for i in range(int(lines)):
    col = list(map(int, input().split()))
    old_array.append(col[:int(cols)])

mean_value = numpy.mean(old_array, axis=1)
var_value = numpy.var(old_array, axis=0)
std_value = numpy.std(old_array, axis=None)
all_values = {"mean": mean_value, "var": var_value, "std": round(std_value, 11)}


for value in all_values.values():
    print(value)