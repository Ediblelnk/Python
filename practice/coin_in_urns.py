import random

def sum(list):
  s = 0
  for i in list:
    s += i
  return s

def simulate(n: int):
  urn = [1, 1]

  for i in range(1, n-1):
    r = random.randint(0, i)
    if r < urn[0]:
      urn[0] += 1
    else:
      urn[1] += 1
  print(urn)

def main():
  n = 1
  while(n != 0):
    n: int = int(input("n: "))
    simulate(n)

if __name__ == '__main__':
  main()