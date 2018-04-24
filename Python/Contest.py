from ContestResult import ContestResult
class Contest(object):

    def __init__(self):
        
        self.contestName = ""
    	self.contestDescription = ""
        self.results = []
        self.id = None
        self.fileName = None
     
    def addResult(self, result):
        if not isinstance(result, ContestResult):
            raise TypeError("result must be of type ContestResult")
    	
        self.results.append(result)
        
    def getResults(self):
        return self.results

    def getName(self):
        return self.contestName

    def getDescription(self):
        return self.contestDescription

