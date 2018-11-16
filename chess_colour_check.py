a = int(input())
b = int(input())
x = int(input())
y = int(input())
if (a + b) % 2 == 0 and (x + y) % 2 == 0:
    print('YES')
elif (a + b) % 2 != 0 and (x + y) % 2 != 0:
    print('YES')
else:
    print('NO')
