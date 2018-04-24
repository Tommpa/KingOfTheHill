import numbers

class ContestResult(object):

    
    def __init__(self, userId, position, score):

        if not isinstance(userId, int):
            raise TypeError("userId must be of type int")

        if not isinstance(position, int):
            raise TypeError("position must be of type int")

        if not isinstance(score, numbers.Number):
            raise TypeError("score must be a number")

        self.userId = userId
        self.position = position
        self.score = score