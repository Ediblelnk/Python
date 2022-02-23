import random
x = 5


#if statements
if x < 0:
	print('negative number')
elif x == 0:
	print('zero')
else:
	print('postive number')
#elif and else parts are optional

#for statements
words = ['cat', 'window', 'definitive value']
for word in words:
	print(word, len(word))
#prints the word and then the number of characters in each word

#range function
for i in range(5): #from 0 inclu to 5 exclu
	print(i)

print(list(range(5, 10, 2)))
#first is starting spot inclu
#second is ending spot exclu
#third is increment

#break statement
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		print(n, 'is a prime number')
#break is used to exit the innermost enclosing for or while loop

#continue statement
for num in range(2, 10):
	if num % 2 == 0:
		print(num, 'is even')
		continue
	print(num, 'is odd')
#continue continues with the next interation of the loop

#pass statement
class empty:
	pass
#pass does nothing, useful for building a skeleton and filling

random_num = random.randint(0, 12)

match random_num:
	case 0:
		print("There is 'nothing' quite like this number")
	case 1:
		print("'One' of the best numbers haha")
	case 2:
		print("This is 'two' funny hehehehehe")
	case _:
		print("I'm sorry I can't count that high!")