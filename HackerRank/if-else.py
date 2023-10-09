n = int(input().strip())
impar = n % 2 != False
if impar:
    status = 'Weird'
elif not impar:
    status = 'Not Weird'
    if (n >= 6) and (n <= 20):
        status = 'Weird'

print(status)
