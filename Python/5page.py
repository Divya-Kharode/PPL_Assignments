i = input("Enter number of inputs:\n")
list1 = []
print "Enter Number in range 0 to 25"
for i in range(0, i):
	num = input()
	if num <= 25:
		list1.append(num)
print list1
print "Missing page numbers are:"
for n in range(1, 26): 
	if n not in list1:
		print(n) 
