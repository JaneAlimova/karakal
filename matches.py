# как решила я
k = int(input())
t = int(input())
z = int(input())
if k == t == z:
    print(3)
elif k != t == z or t != z == k or z != k == t:
    print(2)
elif k != t != z:
    print(0)
    
# как решили разработчики питонтьютор
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
