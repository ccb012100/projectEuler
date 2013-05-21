def euler_3(y):
	# The prime factors of 13195 are 5, 7, 13 and 29.
	# What is the largest prime factor of the number 600851475143 ?



	def prime_test(n):
		flag = True
		
		if n == 2:
			return True
		
		if n % 2 == 0:
			flag = False
			return False
		
		for x in range(3, n/2, 2):
			if x*x > n:
				break
			if n % x == 0:
				return False
			else:
				continue
		
		return True

	def find_primes(a):
	# find nth prime
		x = 2
		largest = 1
		
		while x*x <= a:
			if a % x == 0:
				if prime_test(x) == True:
					largest = x
			x += 1
		
		return largest

	return find_primes(y)
