import random

print "What is your name?"
name = raw_input()

guess_taken = 0
num = random.randint(1, 50)
print name , "We are looking for a number between 1 to 50\n"
while guess_taken < 10:	
	print "Guess a number: "
	guess = input()
	guess = int(guess)
	guess_taken += 1
	if guess < num:
		print("###  Your guess is low  ###")
	if guess > num:
		print("###  Your guess is high  ###")
	if guess == num:
		break;
	
if guess_taken == 10:
	print "No more attempts"	
if guess == num:
	if guess_taken < 3:
		print "Excellent Job", name, "You have guessed a number in", guess_taken, "attempts" 
	if guess_taken < 6:
		print "Average Job", name, "You have guessed a number in", guess_taken, "attempts"
	if guess_taken > 6:
		print "Taken to much time", name, "You have guessed a number in", guess_taken, "attempts" , "Better try next time" 
if guess_taken == 10:
	print "No more attempts"
