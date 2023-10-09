def print_formatted(x):
    intergers = [i for i in range(1, x + 1)]
    octals = [oct(i).removeprefix("0o") for i in range(1, x + 1)]
    hexdecimals = [hex(i).removeprefix("0x").upper() for i in range(1, x + 1)]
    binaries = [bin(i).removeprefix("0b") for i in range(1, x + 1)]

    dohb = list(zip(intergers, octals, hexdecimals, binaries))
    for line in dohb:
        width = len(binaries[x - 1])
        for col in line:
            print(f"{col:>{width}}", end=" ")
        print()


print_formatted(17)
