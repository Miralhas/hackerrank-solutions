import cmath

complex_number = complex(input())
print(round(cmath.polar(complex_number)[0], 3))
print(round(cmath.phase(complex_number), 3))
