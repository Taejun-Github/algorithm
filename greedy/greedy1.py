n = 1260
count = 0
index = 0
coin_type = [500, 100, 50, 10]

for coin in coin_type:
  index = n // coin
  count += index
  n = n - index * coin

print(count)