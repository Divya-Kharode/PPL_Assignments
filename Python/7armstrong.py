lower = int(input("Enter the lower range: \n"))
upper = int(input("Enter the upper range: \n"))

print "Armstrong numbers between", lower , ",", upper, "are :"
for num in range(lower, upper + 1):
	sum = 0
	temp = num
	a = num
	count = 0
	while a > 0:
		count = count + 1
		a = a / 10
	while temp > 0:
		digit = temp % 10
		sum += digit ** count
		temp //= 10
	if num == sum:
		print(num)


