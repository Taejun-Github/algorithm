n, m = map(int, input().split())

result = 0
testList = list()

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  testList.append(min_value)

result = max(testList)
print(result)