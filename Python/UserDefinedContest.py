import sys
import StringIO
from EndomondoParser import EndomondoParser
from Contest import Contest

class UserDefinedContest(Contest):

    def __init__(self, userDefinedContest):
        self.userDefinedContest = userDefinedContest
        self.results = []

        # create file-like string to capture output
        codeOut = StringIO.StringIO()
        codeErr = StringIO.StringIO()
    
        # capture output and errors
        sys.stdout = codeOut
        sys.stderr = codeErr
        try:
            exec(self.userDefinedContest, globals())
            self.contest = UserContest()
            self.contestName = self.contest.contestName
            self.contestDescription = self.contest.contestDescription

        
            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        except:
            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        
            exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default
            traceback_details = {
                             'filename': exc_traceback.tb_frame.f_code.co_filename,
                             'lineno'  : exc_traceback.tb_lineno,
                             'name'    : exc_traceback.tb_frame.f_code.co_name,
                             'type'    : exc_type.__name__,
                             'message' : exc_value.message, # or see traceback._some_str()
                            }
        
            print "Unexpected error:", traceback_details
    
            del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling
            
            self.contest = None
            self.contestName = "User defined contest failed"
            self.contestDescription = "User defined contest failed"

        s = codeErr.getvalue()    
        if len(s) > 0:
            print "error:\n%s\n" % s
    
        s = codeOut.getvalue()
        if len(s) > 0:
            print "output:\n%s" % s
    
        codeOut.close()
        codeErr.close()

        
        

    def calculateUserDefinedScores(self, competitorIds):
        # create file-like string to capture output
        codeOut = StringIO.StringIO()
        codeErr = StringIO.StringIO()
        
        # capture output and errors
        sys.stdout = codeOut
        sys.stderr = codeErr
        try:
            self.contest.calculateScores(competitorIds)
            results = self.contest.getResults()
        
            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        except:
            # restore stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        
            exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default
            traceback_details = {
                             'filename': exc_traceback.tb_frame.f_code.co_filename,
                             'lineno'  : exc_traceback.tb_lineno,
                             'name'    : exc_traceback.tb_frame.f_code.co_name,
                             'type'    : exc_type.__name__,
                             'message' : exc_value.message, # or see traceback._some_str()
                            }
        
            print "Unexpected error:", traceback_details
    
            del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling

        s = codeErr.getvalue()    
        if len(s) > 0:
            print "error:\n%s\n" % s
    
        s = codeOut.getvalue()
        if len(s) > 0:
            print "output:\n%s" % s
    
        codeOut.close()
        codeErr.close()
    
        self.results = results