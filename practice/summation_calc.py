def f(x):
  return 14 * 5**x


s = sum([f(j) for j in range(0,5+1)])

print(s)