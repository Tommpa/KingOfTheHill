import urllib2
import json
import pickle


class EndomondoParser:

	savedWorkouts = {}

	@classmethod
	def getWorkouts(cls, endomondoId):

		# Returns a dict of dicts. For example:
		# {workoutIds: {workoutKey: workoutValue}
		#
		# Practical example on how to extract data:
		#
		# workouts = getWorkouts[endomondoId]
		# for workoutId in workouts:
		#        avg_speed = workouts[workoutId]["speed_avg"])
		#
		#
		#
		# Example of key, value dict returned from a specific workoutId:
		#
		# admin_rejected: False
		# tagged_users: []
		# hashtags: []
		# speed_avg: 10.9220699921
		# weather: {u'type': 2}
		# duration: 974.98
		# sport: 0
		# ascent: 0.0
		# id: 802824758
		# descent: 11.0
		# author: {u'picture': {u'url': u'https://www.endomondo.com/resources/gfx/image/325041/95adbbae34899b12066833a3b9b34fd0/thumbnail.jpg'}, u'first_name': u'Henrik', u'last_name': u'Engdahl', u'middle_name': u'Roadrunner', u'name': u'Henrik Roadrunner Engdahl', u'gender': 0, u'is_premium': False, u'viewer_friendship': 1, u'id': 449427, u'expand': u'abs'}
		# pictures: []
		# is_peptalk_allowed: True
		# points: {u'id': 2199826080310, u'expand': u'ref'}
		# show_workout: 0
		# can_fb_share_via_backend: True
		# speed_max: 16.8802
		# start_time: 2016-09-10T12:12:16.000Z
		# include_in_stats: True
		# altitude_min: 75.7
		# local_start_time: 2016-09-10T14:12:16.000+02:00
		# pb_count: 0
		# hydration: 0.4
		# expand: full
		# distance: 2.95799994469
		# can_copy: False
		# calories: 222.09
		# altitude_max: 98.9
		# is_live: False
		# feed_id: 281475793243539
		# show_map: 1
		
		if len(cls.savedWorkouts) < 1:
			cls.loadFromfileSavedWorkouts()
		
		
		if endomondoId in cls.savedWorkouts:
			return cls.savedWorkouts[endomondoId]
			
		response = urllib2.urlopen('https://www.endomondo.com/embed/user/workouts?id='+str(endomondoId))
		html = response.readlines()
		workouts=[]
		for line in html:
			if(line.find("../../workouts") > 0):
				start=line.find("../../workouts/")+15
				end=line.find("/",start)
				workouts.append(line[start:end])
	
		workouts=set(workouts)
		workoutData={}
	
		for id in workouts:
			urltoopen = "https://www.endomondo.com/rest/v1/users/%s/workouts/%s" %(endomondoId, id)
			#print("urltoopen: " + urltoopen) 
			response=urllib2.urlopen(urltoopen)
			data=json.loads(response.read())
			workoutData[id] = data

		cls.savedWorkouts[endomondoId] = workoutData
		
		cls.saveTofileSavedWorkouts()
		
		return workoutData
	
	@classmethod
	def getUserNameFromEndomondoId(cls, endomondoId):
		if endomondoId not in cls.savedWorkouts:
			cls.getWorkouts(endomondoId)

		# Get a workout. Doesn't matter which workout it is - so just get the "first".
		aWorkout = cls.savedWorkouts[endomondoId][next(iter(cls.savedWorkouts[endomondoId]))]
		return aWorkout['author']['name']
		
	@classmethod
	def saveTofileSavedWorkouts(cls):
		# Saving the objects:
		try:
			f = open('endomondoSave.pckl', 'wb')
			pickle.dump(cls.savedWorkouts, f)
			f.close()
		except:
			pass

	@classmethod
	def loadFromfileSavedWorkouts(cls):
		# Getting back the objects:
		try:
			f = open('endomondoSave.pckl', 'rb')
			cls.savedWorkouts = pickle.load(f)
			f.close()
			print("Using saved data...")
		except:
			pass
	
