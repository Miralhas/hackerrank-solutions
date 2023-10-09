# estudantes = [['Harry', 37.21], ['Berry', 37.22], ['Tina', 37.22], ['Akriti', 41], ['Harsh', 39], ['Na', 37.22], ['Zaaa', 37.2]]
# estudantes = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# estudantes = [['Harry', -50], ['Berry', -50], ['Tina', -50], ['Akriti', 51]]
# estudantes = [[0 for _ in range(2)]for _ in range(int(input()))]
estudantes = []
final = []

for _ in range((int(input()))):
    estudantes.append([input(), float(input())])

tamanho = len(estudantes)
for passo in range(tamanho-1, 0, -1):
    for i in range(passo):
        if estudantes[i][1] > estudantes[i+1][1]:
            aux = estudantes[i+1]
            estudantes[i+1] = estudantes[i]
            estudantes[i] = aux


for i in range(len(estudantes)):
    menor = estudantes[0][1]
    maior = estudantes[-1][1]
    if estudantes[i][1] > menor and estudantes[i][1] < maior:
        final.append(estudantes[i])

while True:
    if final[0][1] < final[-1][1]:
        final.pop()
    else:
        break

print(final)

# final.sort()
# for i in range(len(final)):
#     print(final[i][0])
