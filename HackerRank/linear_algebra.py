import numpy

matrix = []
interger_n = int(input())
for i in range(interger_n):
    new_matrix = input().split()
    matrix.append(list(map(float, new_matrix)))

determinant = round(numpy.linalg.det(matrix), 2)
print(f"{determinant}")