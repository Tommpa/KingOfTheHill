import sys
import StringIO

from UserDefinedContest import UserDefinedContest
from ContestVersionHandler import ContestVersionHandler
from EndomondoParser import EndomondoParser
from Scoring import Scoring

import ContestResult
import Contest
import csv

userIds = [1029317, 449427]

ContestVersionHandler.readContests()
contestIds = ContestVersionHandler.getContestIds()

usernames = map(EndomondoParser.getUserNameFromEndomondoId, userIds)


with open('results.tsv', 'wb') as csvfile:
	headers = ['Contest ID', 'Contest Name']
	resultsWriter = csv.writer(csvfile, delimiter='\t')
	for userId in userIds:
		headers.append('User ID ' + str(userId) + ' Position')
		headers.append('User ID ' + str(userId) + ' Score')
	resultsWriter.writerow(headers)

	for contestId in contestIds:
		
		contestFileName = ContestVersionHandler.getContestFileName(contestId)
		contestFile = open(contestFileName,"r")

		contestCode = contestFile.read()

		contest = UserDefinedContest(contestCode)
		contest.calculateUserDefinedScores(userIds)
		results = contest.getResults()

		print("\n%s (%s) as defined in %s:" %(contest.getName(), contest.getDescription(), contestFileName))
	
		if results is not None:
			for resultEntry in results:
				print("Position %d, %s: %s" %(resultEntry.position, EndomondoParser.getUserNameFromEndomondoId(resultEntry.userId), resultEntry.score))


	
			dataToWrite = ['0', contestFileName]
			if results is not None:
				for resultEntry in results:
					dataToWrite.append(resultEntry.position)
					dataToWrite.append(resultEntry.score)
			
				resultsWriter.writerow(dataToWrite)