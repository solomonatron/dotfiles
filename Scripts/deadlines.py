#deadlines.py
import os
import sys
import time
import datetime

f = open(os.path.expanduser('~') + '/Documents/Deadlines', 'r')

f.seek(0)
line_number = 0
for line in f:
	line_number = line_number + 1
	if (line_number > 2):
		split_line = line.split('-')
		if (len(split_line) > 1):
			#sys.stdout.write(split_line[0].strip())
			split_date = split_line[1].split('/')
			#string = 'python2 -u countdown.py 20' + str(split_date[2].strip()) + ' ' + str(split_date[1].strip()) + ' ' + str(split_date[0].strip()) + ' 12 0'
			#os.system(string)
			#sys.stdout.flush()
			grabyear = int('20' + split_date[2].strip())
			grabmonth = int(split_date[1].strip())
			grabday = int(split_date[0].strip())
			grabhour = 12
			grabminute = 0	
			diff = datetime.datetime(int(grabyear), int(grabmonth), int(grabday), int(grabhour), int(grabminute), 0) - datetime.datetime.today()
			diffy = diff.days/30/12
			diffmo = diff.days/30 - (diff.days/30/12 * 12)
			diffd = diff.days - (diff.days/30 * 30)
			if (diffd == 0):
				diffd = 1
			diffh = diff.seconds/60/60
			diffm = diff.seconds/60 - (diff.seconds/60/60 * 60)
			if (diffy >-1):
				print(split_line[0].strip() + '    ${alignr}' + str(diffy).rjust(1,'0')+'y '+str(diffmo).rjust(2, '0')+'m '+str(diffd).rjust(2,'0')+'d')
			else :
				print(split_line[0].strip() + '    ${alignr}Date Passed')

