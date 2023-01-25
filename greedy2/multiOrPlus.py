string = input()

num_array = list(map(int, list(string)))
num_array.sort()

print(num_array)

result = 0

for i in num_array:
  if i <= 1 or result <= 1:
    result += i
  else:
    result *= i


print(result)