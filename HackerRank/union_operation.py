english_students = int(input())

english_newspaper = input().split()
english_newspaper = set(english_newspaper[:english_students])

french_students = int(input())
french_newspaper = input().split()
french_newspaper = set(french_newspaper[:french_students])

one_sub = english_newspaper.union(french_newspaper)

print(len(one_sub))