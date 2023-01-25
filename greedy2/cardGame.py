n, m = map(int, input().split())

min_value = []

for i in range(n):
  data = list(map(int, input().split()))
  data.sort()
  min = data[0]
  min_value.append(min)

min_value.sort()
print(max(min_value))

