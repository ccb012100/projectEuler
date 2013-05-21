def euler_6():
	# The sum of the squares of the first ten natural numbers is,
	#    1^2 + 2^2 + ... + 10^2 = 385
	# The square of the sum of the first ten natural numbers is,
	#     (1 + 2 + ... + 10)^2 = 552 = 3025
	# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
	# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	sum1 = 0
	sum2 = 0
	for x  in range(1,101):
		sum1 += pow(x,2)
		sum2 += x
	diff = pow(sum2,2) - sum1
	print "The difference is", diff
