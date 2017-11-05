animals = ['cat','dog']

for a in animals[:]:
	if len(a) > 2:
		animals.insert(0,a)
	
print animals