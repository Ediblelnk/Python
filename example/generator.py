def infinite_sequence(x = 0):
  while True:
    x = yield x+1

print(next(infinite_sequence))
print(next(infinite_sequence))
print(next(infinite_sequence))
print(next(infinite_sequence))