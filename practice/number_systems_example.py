from number_systems import Quaternion, UnitQ

a = Quaternion(1, 2, 1, 2)
b = Quaternion(-3, 4, -1, 2)

print(f'a = {a}', f'b = {b}', sep='\n')
print(f'a + b = {a+b}', sep='\n')
print(f'a * b = {a*b}', f'b * a = {b*a}', sep='\n')
