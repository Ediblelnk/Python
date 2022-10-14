import itertools

letters = set()

i = ""

while(i != "exit"):
  i = input("Input: ")
  for l in i:
    letters.add(l)
  print(letters)
print("Finished with that! Next!")

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}
C = {x for x in A if x not in B}

print('A:', A)
print('B:', B)
print('C:', C)

print('A | B :', A | B)
print('A & B :', A & B)
print('A - B :', A - B)
print('B - A :', B - A)
print('A ^ B :', A ^ B)

F = {1, 2}
G = {'a', 'b', 'c'}
result = set(itertools.product(A, B))

print('Cartesian Product of A and B:', result)