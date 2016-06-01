import subprocess
import os
from pprint import pprint


days = ["su", "mo", "tu", "we", "th", "fr", "sa"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
startYear = 2008
endYear = 2042 #exclusive


# def getDaysData():
# 	data = dict()
# 	for year in range(startYear, endYear):
# 		data[year] = dict()
# 		for month in months:
# 			data[year][month] = dict()
# 			# count_c = 0
# 			cal_data = subprocess.Popen("cal " + str(month) + " " + str(year),shell=True, stdout=subprocess.PIPE)

# 			week_loop = 0
# 			for line in iter(cal_data.stdout.readline, b""):
# 				if week_loop > 1: #this is after month name and day_names
# 					char_num = 0
# 					day = 0
# 					date = ""
# 					for c in line:
# 						date += c
# 						if char_num > 1: #every three characters
# 							char_num = 0
# 							if len(date.strip()) > 0: #somefields are blank in each month's first week
# 								data[year][month][int(date)] = days[day]
# 							date = ""
# 							day += 1
# 						else:
# 							char_num += 1
# 				week_loop += 1
# 	return data


# data = getDaysData()

# # PRINTING
# writer = open("out.txt", "w")
# month_c_lengths = dict()
# old_len_s = 0



# first_year = True
# for year in range(startYear, endYear):

# 	# print year
# 	s = "|"
# 	for month in months:
# 		# print month
# 		# print " ",
# 		s += " "
# 		for day in data[year][month]:
			
# 			if data[year][month][day] is "su":
# 				# print "*  ",
# 				if day < 10:
# 					s += " * "
# 				else:
# 					s += " *  "
# 			else:
# 				# print day, " ",
# 				s += " " + str(day) + " "

# 		# print "|", len(data[year][month])
# 		if month is "February" and len(data[year][month]) is 28:
# 			s += "    "
# 		s += " |"
# 		if month is "June":
# 			s += "|  " + str(year) + "  ||"

# 	# print s
# 		if first_year:
# 			if month not in month_c_lengths:
# 				month_c_lengths[month] = len(s) - old_len_s
# 			old_len_s = len(s)


# 	if first_year:
# 		month_str = ""
# 		for month in months:
# 			# print month, month_c_lengths[month]
# 			blank_length = month_c_lengths[month]/2 - len(month)/2
# 			for i in range(blank_length):
# 				month_str += " "
# 			month_str += str(month)	
# 			for i in range(blank_length):
# 				month_str += " "

# 		# print month_str
# 		writer.write(month_str)
# 		writer.write("\n\n")

# 	s_blank = ""
# 	for c in s:
# 		if c is not "|":
# 			s_blank += "-"
# 		else:
# 			s_blank += c
# 	writer.write(s_blank)
# 	writer.write("\n")
# 	writer.write(s)
# 	writer.write("\n")

# 	s = ""
# 	first_year = False

# writer.write(s_blank)
# writer.write("\n")
# writer.write("\n")
# writer.write(" * = Sundays")
# writer.write("\n")

# writer.close()
# # print month_c_lengths
# print "done"



def getDaysData():
	writer = open("out.txt", "w")
	first_year = True
	dividing_line = ""
	decade_divider = ""

	data = dict()
	for year in range(startYear, endYear):
		
		s = "|"

		# data[year] = dict()
		for month in months:

			s += " "

			# data[year][month] = dict()

			cal_data = subprocess.Popen("cal " + str(month) + " " + str(year),shell=True, stdout=subprocess.PIPE)

			week_loop = 0
			for line in iter(cal_data.stdout.readline, b""):
				if week_loop > 1: #this is after month name and day_names
					char_num = 0
					day = 0
					date = ""
					for c in line:
						date += c
						if char_num > 1: #every three characters
							char_num = 0
							if len(date.strip()) > 0: #somefields are blank in each month's first week
								# data[year][month][int(date)] = days[day]
								if days[day] is "su":
									if int(date) < 10:
										s += " * "
									else:
										s += " *  "
								else:
									s += " " + str(date.strip()) + " "

							date = ""
							day += 1
						else:
							char_num += 1
				week_loop += 1

			print len(s)
			if month is "February" and len(s) is 223:
				s += "    "
			s += " |"
			if month is "June":
				s += "|  " + str(year) + "  ||"
		print s

		if first_year is True:
			first_year = False
			for c in s:
				if c is not "|":
					dividing_line += "-"
					decade_divider += "="
				else:
					dividing_line += c
					decade_divider += c

		if str(year)[-1] is "1":
			writer.write(decade_divider)
			writer.write("\n")
			writer.write(decade_divider)
		else:
			writer.write(dividing_line)
		writer.write("\n")
		writer.write(s)
		writer.write("\n")

	writer.close()

getDaysData()

