print "Tic tac toe outline:"

places = {'TL':'','TM':'','TR':'','ML':'','MM':'','MR':'','LL':'','LM':'','LR':''}
display = {}

def printPlaces( place, value):
	display = dict(places)
	display[place] = value
	for values in display:
		if display[values] == 1:
			display[values] = 'X'
		elif display[values] ==10:
			display[values] = 'O'
				
			
	print  display['TL'] ,"|", display['TM'] ,"|", display['TR'] 
	print "---------"
	print  display['ML'] ,"|", display['MM'] ,"|", display['MR'] 
	print "---------"
	print  display['LL'] ,"|", display['LM'] ,"|", display['LR']
	
def userInput():

	place = raw_input("Which place? ")
	places[place] = 1
	return place

def myTurn(userplace):
	place = ''
	if places['MM'] == '':
		places['MM'] = 10
		place = 'MM'
#	if not places['LL']+places['LM']+places['LR'] == 20:
#		if places['LL']+places['userplace'] == 20:
#			places['LM'] = 10
#			place = 'LM'
		
	return place

print  places['TL'] ,"|", places['TM'] ,"|", places['TR'] 
print "---------"
print  places['ML'] ,"|", places['MM'] ,"|", places['MR'] 
print "---------"
print  places['LL'] ,"|", places['LM'] ,"|", places['LR'] 

uplace = userInput()
printPlaces( uplace,'X')

print "My Turn: "

place = myTurn(uplace)
printPlaces( place,'O')

uplace = userInput()
printPlaces( uplace,'X')

print "My Turn: "

place = myTurn(uplace)