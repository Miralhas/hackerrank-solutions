a_size = int(input())
a_set = set(map(int, input().split()[:a_size]))
b_size = int(input())
b_set = set(map(int, input().split()[:b_size]))

same_values = a_set.intersection(b_set)
all_values = a_set.union(b_set)
for value in sorted(all_values):
    if value not in same_values:
        print(value)
