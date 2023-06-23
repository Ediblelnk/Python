import math
import time

#timer decorator function
def functionTimer(function):
	def timeIt(*args, **kwarg):
		start = time.time()
		function(*args, **kwarg)
		print((time.time()-start)*1000, "ms")
	return timeIt

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


#returns if a num is prime or not
def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	else:
		return False

betterPrimeIn(1_000_000)