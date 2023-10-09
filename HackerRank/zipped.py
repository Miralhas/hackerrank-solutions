estudantes, subjects = list(map(int, input().split()))
all_subjects = []

for i in range(subjects):
    all_subjects.append(list(map(float, input().split())))

all_subjects = list(zip(*all_subjects))
averages = []

for student_grade in all_subjects:
    student_average = round((sum(student_grade) / subjects), 1)
    averages.append(student_average)

for average in averages:
    print(average)