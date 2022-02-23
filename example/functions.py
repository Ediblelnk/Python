#keyword def introduces a function definition
#must be follow by function name and list of parameters
def fib(n):
	a, b = 0, 1 #fib seeds
	while a < n:
		print(a, end=' ')
		a, b = b, a +b
	print()

fib(100)

#fib function that put the numbers into a list
def fibList(n):
	result = []
	a, b = 0, 1 #fib seeds
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

print(fibList(100))

#variable number of arguments
def askOk(prompt, retries=4, reminder='try again'):
	while retries > 0:
		response = input(prompt)
		if response in ('y', 'ye', 'yes'):
			return 'ok'
		if response in ('n', 'no', 'nope'):
			return 'not ok'
		retries -= 1
		if retries > 0:
			print(reminder)
	return 'unknown condition'

#default value is evaluated only once
def f(a, L=[]):
	L.append(a)
	return L

print(f(10))
print(f(5))
#the list persists through different calls

#keyword arguments
def power(a=0, pow=1):
	print(a**pow)

power(3)
power(3, 4)
power(pow=4, a=4) #keywords need not be in precise order

# *parameters
def strung(cheese, *wine): # *wine represents tuple containing positional arguments beyond formal parameter list
	print('I would like some', cheese) # a *parameter must come before a **parameter
	print('-' * 25)
	print('We also have:')
	for kind in wine:
		print(kind, 'wine', end=', ')
	print()

strung('cheddar', 'white', 'red', 'rose')

print()

# **parameters
def snack(cracker, **drink):
	print(cracker, 'are very tasty with:')
	for kind in drink:
		print(f'{drink[kind]} {kind}')

snack('saltines', salad='american', cheese='american', tea='lemon')