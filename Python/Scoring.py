class WinnerScoring(object):
	
	def __init__(self):
		pass
	
	def getWinnerScore(self, positionInContest):
		score = {1: 25,
				2: 18,
				3: 15,
				4: 12,
				5: 10,
				6: 8,
				7: 6,
				8: 4,
				9: 2,
				10: 1}
		if positionInContest in score:
			return score[positionInContest]
		else:
			return 0
			