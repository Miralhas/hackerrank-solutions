import numpy
numpy.set_printoptions(legacy='1.13')

lines, cols = input().split()

print(numpy.eye(int(lines), int(cols)))