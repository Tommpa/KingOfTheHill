import urllib2
import json
endomondoid=449427

response = urllib2.urlopen('https://www.endomondo.com/embed/user/workouts?id='+str(endomondoid))
html = response.readlines()
workouts=[]
for line in html:
    if(line.find("../../workouts") > 0):
        start=line.find("../../workouts/")+15
        end=line.find("/",start)
        workouts.append(line[start:end])

workouts=set(workouts)

for id in workouts:
    response=urllib2.urlopen("https://www.endomondo.com/rest/v1/users/449427/workouts/"+id)
    data=json.loads(response.read())
    for key in data:
        print("%s: %s" %(key,data[key]))
    print("\n\n\n")