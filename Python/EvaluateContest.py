import sys
import StringIO


# create file-like string to capture output
codeOut = StringIO.StringIO()
codeErr = StringIO.StringIO()

contestFile = open("Endomondo_TF.py","r")
contestCode = contestFile.read()

# capture output and errors
sys.stdout = codeOut
sys.stderr = codeErr
try:

    exec contestCode
    print calculateScores(competitorIds = [1029317, 449427])

    # restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
except:
    # restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    print "Unexpected error:", sys.exc_info()#[0]

# Evaluate the user defined code
s = codeErr.getvalue()

print "error:\n%s\n" % s

s = codeOut.getvalue()

print "output:\n%s" % s

codeOut.close()
codeErr.close()