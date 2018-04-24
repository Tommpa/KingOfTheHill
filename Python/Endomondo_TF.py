def calculateScores(competitorIds):

    from dateutil import parser as timeparser
    from datetime import datetime
    from Contest import Contest
    from ContestResult import ContestResult

    contestName = "Max speed"
    contestExplanation = "Results are based on maximum speed during the last month."

    contest = Contest(contestName, contestExplanation)
    print contest
    scores = []
    
    for competitorId in competitorIds:
        max_speed = 0
        workouts = EndomondoParser.getWorkouts(competitorId)

        #print "*************"
        #print workouts
        #print "*************"
        
        currentDatetime = datetime.now()

        for workoutId in workouts:
            workoutDatetime = timeparser.parse(workouts[workoutId]['local_start_time'])
            if (workoutDatetime.year == currentDatetime.year) and (workoutDatetime.month == currentDatetime.month-1):
                max_speed = max(max_speed, workouts[workoutId]["speed_avg"])

        scores.append((competitorId, max_speed))

    sortedScores = sorted(scores, key=lambda scores: scores[1], reverse = True)

    print sortedScores

    position = 0
    lastScore = None
    for competitorId, max_speed in sortedScores:
        score = max_speed
        if score != lastScore:
            position = position + 1

        tempResult = ContestResult(competitorId, position, score)
        contest.addResult(tempResult)

        lastScore = score 
    
    print contest       
    return contest