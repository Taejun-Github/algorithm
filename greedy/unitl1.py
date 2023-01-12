n, k = map(int, input().split())
index = 0

while n > 1:
  if n % k == 0:
    n = int(n / k)
    index += 1
  else:
    n -= 1
    index += 1
print(index)
  