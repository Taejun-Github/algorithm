n = int(input())
array = [0] * 1001

for i in range(3, n+1):
  array[1] = 1
  array[2] = 3
  array[i] = array[i-1] + array[i-2] * 2

print(array[100])