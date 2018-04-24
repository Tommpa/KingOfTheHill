import sys
import StringIO

from UserDefinedContest import UserDefinedContest
import ContestResult
import Contest

from EndomondoParser import EndomondoParser

users = [1029317, 449427]
contestFileNames = ["Endomondo_TF3.py","Endomondo_TF2.py"]

for contestFileName in contestFileNames:
	contestFile = open(contestFileName,"r")

	contestCode = contestFile.read()

	contest = UserDefinedContest(contestCode)
	contest.calculateUserDefinedScores(users)
	results = contest.getResults()

	print("\n%s (%s) as defined in %s:" %(contest.getName(), contest.getDescription(), contestFileName))
		
	if results is not None:
		for resultEntry in results:
			print("Position %d, %s: %s" %(resultEntry.position, EndomondoParser.getUserNameFromEndomondoId(resultEntry.userId), resultEntry.score))
