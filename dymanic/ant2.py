x = int(input())
n = map(int, input().split())

array = [0] * 100

array[0] = array[0]
array[1] = max(array[0], array[1])

for i in range(2, n):
  array[i] = max(array[i-1], array[i-2] + array[i])

print(array[n-1])
