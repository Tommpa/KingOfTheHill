import sys
import StringIO

from UserDefinedContest import UserDefinedContest
from ContestVersionHandler import ContestVersionHandler
from EndomondoParser import EndomondoParser
from Scoring import WinnerScoring

import ContestResult
import Contest
import csv

userIds = [1029317, 449427]



ContestVersionHandler.readContests()
contestIds = ContestVersionHandler.getContestIds()

usernames = map(EndomondoParser.getUserNameFromEndomondoId, userIds)

positionToScore = WinnerScoring()
contestFileName = {}
contestName = {}
contestCode = {}
contest = {}
results = {}


# --- Evaluate contests

for contestId in contestIds:
		
	contestFileName[contestId] = ContestVersionHandler.getContestFileName(contestId)
	contestName[contestId] = ContestVersionHandler.getContestName(contestId)
	contestFile = open(contestFileName[contestId],"r")
	contestCode[contestId] = contestFile.read()

	contest[contestId] = UserDefinedContest(contestCode[contestId])
	contest[contestId].calculateUserDefinedScores(userIds)
	results[contestId] = contest[contestId].getResults()


# --- Create users.tsv file ---

with open('users.tsv', 'wb') as usersFile:
	headers = ['User ID', 'User Name']
	usersFileWriter.writerow(headers)
	for userId in userIds:
		usersFileWriter.writerow([userId, EndomondoParser.getUserNameFromEndomondoId(resultEntry.userId)])

# --- Create results.tsv file ---
				
with open('individualContestResults.tsv', 'wb') as individualContestResultsFile:
	headers = ['Contest ID', 'Contest Name']
	individualContestResultsWriter = csv.writer(individualContestResultsFile, delimiter='\t')
	for userId in userIds:
		headers.append(str(userId) + ' Position')
		headers.append(str(userId) + ' ContestScore')
		headers.append(str(userId) + ' WinnerScore')
	individualContestResultsWriter.writerow(headers)
	for contestId in contestIds:
		if results[contestId] is not None:
			for resultEntry in results[contestId]:
				print("Position %d, %s: %s" %(resultEntry.position, EndomondoParser.getUserNameFromEndomondoId(resultEntry.userId), resultEntry.score))
	
			dataToWrite = [contestId, contestName[contestId]]
			if results[contestId] is not None:
				for resultEntry in results[contestId]:
					dataToWrite.append(resultEntry.position)
					dataToWrite.append(resultEntry.score)
					dataToWrite.append(positionToScore.getWinnerScore(resultEntry.position))
				individualContestResultsWriter.writerow(dataToWrite)


