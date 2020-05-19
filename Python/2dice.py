import random

rolling = True
s = 0
while rolling:
	roll_again = raw_input("Ready to Roll? Enter = Roll, Q = Quit\n")
	if roll_again.lower() != "q":
		r = random.randint(1,6)
		print "Rolled Number is ", r
		s = s + r
	else:
		rolling = False
print "Total = ", s

print "Thanks For Playing"      
