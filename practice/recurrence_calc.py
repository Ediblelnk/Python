def f(n):
  if n == 1:
    return 5
  return(f(n-1) + 2*n)

if __name__ == '__main__':
  print(f(2))