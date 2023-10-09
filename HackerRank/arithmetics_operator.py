# n = int(input())
# arr = map(int, input().split())
from random import randint

scores = [randint(2,9) for x in range(10)]
scores.sort()
second_runner = []

for score in scores:
    if score < max(scores):
        second_runner.append(score)

while len(second_runner) != 1:
    second_runner.pop(0)

second = second_runner[0]
print(f"second = {second} \nfirst = {max(scores)}")