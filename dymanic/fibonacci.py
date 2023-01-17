d = [0] * 100

def fibo(x):
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

def fibo2(x):
  d2 = [0] * x
  for i in range(x):
    if i == 0 or i == 1:
      d2[i] = 1
    else:
      d2[i] = d2[i-1] + d2[i-2]
  return d2

print(fibo2(99))