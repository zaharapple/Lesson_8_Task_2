# Переделать вторую задачу так, чтобы результат писался в другой файл

f = open('test.py', 'r')
res = open('result.py', 'w') #если файла не существует, создается новый

for line in f:
    b=list(map(int, line.split()))

    fizz = int(b[0])
    buzz = int(b[1])
    value3 = int(b[2])
    print(' ')

    for i in range(1, value3 + 1):
        if (i % fizz == 0) and (i % buzz == 0):
            print('FB', end=" ", file=res)
        elif i % fizz == 0:
            print("F", end=" ", file=res)
        elif i % buzz == 0:
            print('B', end=" ", file=res)
        else:
            print(i, end=" ", file=res)
    print("\n", end="", file=res)
f.close()
res.close()
print('Everything is recorded in result.py')
