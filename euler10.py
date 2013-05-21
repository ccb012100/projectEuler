def euler_10():
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    # Find the sum of all the primes below two million.
	import math

	def prime_test(n):
		flag = True

		m = int(math.sqrt(n))

		if n == 2:
			return True

		if n % 2 == 0:
			flag = False
			return False

		for x in range(3, m+1, 2):
			if n % x == 0:
				return False
			else:
				continue

		return True

	def find_primes(a):
	# find nth prime
		x = 2
		sum = 0

		while x < a:
			if prime_test(x) == True:
				sum += x
			x += 1

		return sum

	y = 2000000
	print find_primes(y)
