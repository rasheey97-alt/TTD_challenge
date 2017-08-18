filename ="port-harcourt-weather.txt"
with open(filename) as file:
	next(file)
	next(file)
	dailyList= []
	dailyTempSpread=[]
	for line in file:
		splitted_line = line.split()

		#if isinstance(splitted_line[0], int):

		 #print splitted_line[0],splitted_line[1]


		
		
		try:
			dayListNUM =int(splitted_line[0])
			dailyHigh= int(splitted_line[1])
			dailyLow= int(splitted_line[2])
			
			#dailyTempSpread.append (dailyHigh-dailyLow)
			# int (splitted_line[0])

		except  ValueError:

			pass
		dailyTempSpread.append (dailyHigh-dailyLow)
		dailyList.append(dayListNUM)

		
		
		#print len(dailyList)
		#print len(dailyTempSpread)
weatherDict=dict(zip(dailyList, dailyTempSpread))
#print  weatherDict
print dayListNUM
print splitted_line[0]