N = int(input())
M = int(input())
x = int(input())
y = int(input())
mmax = max(N, M)
mmin = min(N, M)
N = mmax - y
M = mmin - x
print(min(x,y,M,N))

#решение не мое, но оно было самым интересным из всех, что я нашла (и правильным, разумеется)
