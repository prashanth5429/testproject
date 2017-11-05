print "\nInventory:\n"

inventory = {"Rope":12, "Ladder":2, 'bucket':3}
total = 0
for k,v in inventory.items():
	print k,":",v
	total = total + v

print "\n Total items: ",total