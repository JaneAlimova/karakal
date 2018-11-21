# мое решение:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a - 1 <= c <= a + 1 and b - 1 <= d <= b + 1:
    print('YES')
else: print('NO')

# решение разработчиков:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')
