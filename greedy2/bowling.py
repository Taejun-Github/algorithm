n, m = map(int, input().split())

k = list(map(int, input().split()))
k.sort()

count = 0


for i in k:
  first = i
  for j in k:
    if j == i:
      continue
    else:
      count += 1

print(int(count / 2)) 