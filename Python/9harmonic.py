count = 0
n = 1
sum1 = 0.0
harmonic = 0.0
l = 0
while count < 10:
	sum1 = 0
	l = 0
	for i in range(1, n + 1):
		if n % i == 0:
			if float(n) // i == i:  
				sum1 += float(n) / i	  
				l += 1
            		else:  
                		sum1 += float(n) / i	  
                		sum1 += float(n) / (float(n) // i) 
				l += 2
	sum1 = sum1 / n	
	harmonic = l / sum1
	nu = int(harmonic)
	if harmonic == nu:
		print n
		count += 1
	n += 1
	
