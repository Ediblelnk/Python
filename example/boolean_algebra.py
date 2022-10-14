x = True
y = True

print('x: ', x)
print('y: ', y)

def adder4(x: bool, y: bool):
  print("x: ", x, "| y: ", y)
  h = x and y
  l = (not x and y) or (not y and x)
  print("h: ", h, "| l: ", l)

adder4(x, y)