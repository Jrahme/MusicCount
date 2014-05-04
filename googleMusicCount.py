from gmusicapi import Mobileclient
api = Mobileclient()
#not going to work because of two step authentication, need to set up an app specific password
logged_in = api.login('your email','email or a google app password')

songs = api.get_all_songs(False,False)


totalTime = 0


for key in songs:
	totalTime = totalTime+ (float(key['durationMillis']) / 1000) * key['playCount']

totalMinutes = totalTime/60
totalHours = totalMinutes/60
totalDays = totalHours/24
hours = (totalDays - int(totalDays)) * 24
minutes = (hours - int(hours)) * 60
seconds = (minutes - int(minutes)) * 60

print "I have played %01d days, %01d hours, %01d minutes, %01d seconds of music on my google play account"%(totalDays,hours,minutes,seconds)
print "This is a total of %01d hours"%(totalHours)
