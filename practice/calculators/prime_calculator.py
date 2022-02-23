import math
import time

#timer decorator function
def functionTimer(function):
	def timeIt(*args, **kwarg):
		start = time.time()
		function(*args, **kwarg)
		print(time.time()-start)
	return timeIt

#prints primes in input range
@functionTimer
def brutePrimeIn(bound):
	total = 0
	for num in range(2, bound):
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			total += 1
	print('brutePrimeIn', total, sep=', ')

@functionTimer
def betterPrimeIn(bound):
	total = 0
	for num in range(1, bound, 2):
		for i in range(2, int(math.sqrt(num))+1):
			if num % i == 0:
				break
		else:
			total += 1
	print('betterPrimeIn', total, sep=', ', end='; ')

@functionTimer
def listPrimeIn(bound):
	primelist = [2]
	for num in range(3, bound, 2):
		for prime in primelist:
			if num%prime == 0:
				break
		else:
			primelist.append(num)
	print('listPrimeIn', len(primelist), sep=', ', end='; ')


#returns if a num is prime or not
def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	else:
		return False

betterPrimeIn(100000)
listPrimeIn(100000)