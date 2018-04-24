from Contest import Contest

class UserContest(Contest):

    def __init__(self):
        self.contestName = "Like a Yoyo"
        self.contestDescription = "Results are based on the summary of this month's ascent and descent."
        self.results = []

    def calculateScores(self, competitorIds):
    
        from dateutil import parser as timeparser
        from datetime import datetime
        #from Contest import Contest
        from ContestResult import ContestResult

        scores = []
    
        for competitorId in competitorIds:
            upAndDown = 0
            workouts = EndomondoParser.getWorkouts(competitorId)
       
            currentDatetime = datetime.now()

            for workoutId in workouts:
                workoutDatetime = timeparser.parse(workouts[workoutId]['local_start_time'])
                if (workoutDatetime.year == currentDatetime.year) and (workoutDatetime.month == currentDatetime.month-1):
                    upAndDown = upAndDown + workouts[workoutId]["ascent"] + workouts[workoutId]["descent"]

            scores.append((competitorId, upAndDown))

        sortedScores = sorted(scores, key=lambda scores: scores[1], reverse = True)

        position = 0
        lastScore = None
        for competitorId, score in sortedScores:
            if score != lastScore:
                position = position + 1

            tempResult = ContestResult(competitorId, position, score)
            self.addResult(tempResult)

            lastScore = score 

