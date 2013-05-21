def euler_4():
	import sys
	#A palindromic number reads the same both ways.
	#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
	#Find the largest palindrome made from the product of two 3-digit numbers.
	x = 999
	y = 999
	flag = 0
	ans = 0
	while x > 99:
		while y > 99:
			num = x*y
			if str(num) == str(num)[::-1]:
				if num > ans:
					ans = num
				break
			else:
				y -= 1
		y = 999
		x -= 1
	print ans, "is the product of", x, "and", y, "."
