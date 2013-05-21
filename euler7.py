def euler_7(q):
	# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

	# What is the 10,001st prime number?

	def prime_test(a):
		
		flag = True
		
		if a == 2:
			return True
		
		if a % 2 == 0:
			flag = False
			return False
		
		for x in range(3, a/2, 2):
			if x*x > a:
				break
			if a % x == 0:
				return False
			else:
				continue
		
		return True

	def find_primes(n):
	# find nth prime
		count = 0
		x = 2
		l = []
		
		while count < n:
			if prime_test(x) == True:
				l.append(x)
				count += 1
			x += 1
			
		return l
		
	return find_primes(q)
