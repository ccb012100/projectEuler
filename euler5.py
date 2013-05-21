def euler_5():
	# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

	flag = 0
	x = 2520
	while flag == 0:
		x += 2
		for y in range(1, 21):
			if x % y == 0:
				flag = 1
			else:
				flag = 0
				break
	print x, "is the smallest number divisible by the numbers 1 to 20"
