n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

a = m // (k + 1)
b = m % (k + 1)

ans = ((first * k) + second) * a + first * b
print(ans)