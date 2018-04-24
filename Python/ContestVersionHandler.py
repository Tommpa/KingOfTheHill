import csv

class ContestVersionHandler:

	contests = {}
	fieldNames = ['ContestId', 'Version', 'ContestName', 'FileName']
	
	@classmethod
	def readContests(cls):
		with open('contests.tsv') as csvfile:
			reader = csv.DictReader(csvfile, delimiter='\t')
			for row in reader:
				if row['ContestId'] not in cls.contests:
					cls.contests[row['ContestId']] = {}
				cls.contests[row['ContestId']][row['Version']] = {'ContestName': row['ContestName'], 'FileName': row['FileName']}
		return cls.contests

	@classmethod
	def addNewVersionOfContest(cls, contestId):
		with open('contests.tsv') as csvfile:
			contestWriter = csv.DictWriter(csvfile, fieldnames=cls.fieldNames)
			newContestVersion = {}
			newContestVersion['ContestId'] = contestId
			newContestVersion['Version'] = cls.getLatestVersionOfContests(contestId) + 1
			newContestVersion['ContestName'] = cls.getContestName(contestId)
			newContestVersion['FileName']  = cls.generateContestFileName(contestId, newContestVersion['Version'])
			contestWriter.writerow(newContestVersion)

	@classmethod
	def getNewContestId(cls):
		newContestId = max(cls.getContestIds()) + 1
		return newContestId

	@classmethod
	def getContestIds(cls):
		return(cls.contests.keys())

	@classmethod
	def getLatestVersionOfContests(cls, contestId):
		versions = cls.contests[contestId].keys()
		return(max(versions))

	@classmethod
	def generateContestFileName(cls, contestId, version):
		fileName = str(contestId) + "_v" + str(version)
		return fileName

	@classmethod
	def getContestFileName(cls, contestId, version = None):
		if version is None:
			version = cls.getLatestVersionOfContests(contestId)
		return cls.contests[contestId][version]['FileName']
		
	@classmethod
	def getContestName(cls, contestId, version = None):
		if version is None:
			version = cls.getLatestVersionOfContests(contestId)
		return cls.contests[contestId][version]['ContestName']
	