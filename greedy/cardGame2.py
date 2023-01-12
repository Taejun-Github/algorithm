n, m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10000
  for a in data:
    min_value = min(min_value, a)
    