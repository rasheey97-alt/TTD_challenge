filename = "football-league-results.txt"
def leagueResult():
	with open (filename) as result:
	            clubName =[]
	            result.next()
	            clubGoalDiff =[]            
	            newResult= []
	            # tempGoalFor = []
	            # tempGoalAgainst = []
	            for team in result:
	                team = team.split()
	                teamName = []
	                teamData = []
	                for data in team:
	                    try:
	                        data = int(data)
	                        teamData.append(data)
	                        pass
	                    except ValueError:
	                        stringName = str(data)
	                        if stringName != "-":
	                            teamName.append(stringName)
	                        pass
	                if len(teamData) > 0:
	                    goalFor = teamData[4]
	                    goalAgainst = teamData[5]
	                    del teamName[:1]
	                    teamName = ''.join(teamName)
	                    clubName.append(teamName)
	                    diffGoal = goalFor - goalAgainst
	                    clubGoalDiff.append(diffGoal)
	                
	            clubGoalPerfomance = dict(zip(clubName, clubGoalDiff))
	            teamWithLowestGoalDiff = min(sorted(clubGoalPerfomance.keys()))
	            lowestGoalDiff = min(sorted(clubGoalPerfomance.values()))
	            teamWithLowestGoalDiff = str(teamWithLowestGoalDiff)
	            lowestGoalDiff = str(lowestGoalDiff)
	            
	            print "The Club with the lowest goal difference is " + teamWithLowestGoalDiff + ", with: " + lowestGoalDiff + " goal difference"


leagueResult()

