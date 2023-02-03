def f(n):
  if n == 0:
    return 2
  if n == 1:
    return 5
  return f(n-1) * f(n-2)

if __name__ == '__main__':
  print(f(3))