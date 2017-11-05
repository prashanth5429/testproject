def collatz(number):
	
	if number%2 == 0:
		print number//2
		return number//2
	if number%2 ==1:
		print 3*number+1
		return 3*number+1


while True:		
	try:
		no = int(raw_input())
		if 1==collatz(no):
			break
	except :
		print "Enter only number."
	