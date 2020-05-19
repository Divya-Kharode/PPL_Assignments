i = 0;
count = 0;
while count < 20 :
	sum1 = 0
	sum2 = 0
	flag = 0
	for k in range(1,i):
		if(i % k == 0):
			sum1 += k
	j = sum1
	for m in range(1, sum1):
		if(j % m == 0):
			sum2 += m
	if sum2 == i and sum1 == j and sum1 != sum2:
		flag = 1
		if count % 2 == 0:	
			print i,j
		count += 1
	i += 1	
		
