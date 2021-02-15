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
            res.write('FB ')
        elif i % fizz == 0:
            res.write('F ')
        elif i % buzz == 0:
            res.write('B ')
        else:
            res.write(str(i) + ' ')
    res.write('\n')
f.close()
res.close()
print('Everything is recorded in result.py')
