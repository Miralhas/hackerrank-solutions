arr = []
commands = []
datas = []
for i in range(int(input())):
    data = input().split()
    commands.append(data[0])
    data.remove(data[0])
    datas.append(data)

for i, command in enumerate(commands):
    if command == "insert":
        arr.insert(int(datas[i][0]), int(datas[i][1]))
    elif command == "print":
        print(arr)
    elif command == "remove":
        arr.remove(int(datas[i][0]))
    elif command == "append":
        arr.append(int(datas[i][0]))
    elif command == "sort":
        arr.sort()
    elif command == "pop":
        arr.pop()
    elif command == "reverse":
        arr.reverse()
