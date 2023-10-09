import numpy    

old_array = []
lines, cols = input().split()

for i in range(int(lines)):
    col = list(map(int, input().split()))
    old_array.append(col[:int(cols)])

my_array = numpy.array(old_array)
min_value = numpy.min(my_array, axis=1)
max_value = numpy.max([min_value], axis=1)
print(max_value[0])