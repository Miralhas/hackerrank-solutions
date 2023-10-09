students = []
scores = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    scores.append(score)
    students.append([name, score])

second_lowest = sorted(set(scores))[1]

students.sort()
for student in students:
    if student[1] == second_lowest:
        print(student[0])