x1 = int(input('сколько человек в 1 классе: '))
x2 = int(input('сколько человек во 2 классе: '))
x3 = int(input('сколько человек в 3 классе: '))
import math
a = math.ceil(x1 / 2)
b = math.ceil(x2 / 2)
c = math.ceil(x3 / 2)
x = (a + b + c)
print(x)
