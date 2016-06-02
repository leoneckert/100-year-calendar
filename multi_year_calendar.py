import subprocess
import os
from pprint import pprint
import sys



days = ["su", "mo", "tu", "we", "th", "fr", "sa"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# startYear = 1990
# year_interval = 100
# endYear = startYear + year_interval 



def getDaysData(startYear, endYear):
	writer = open(str(startYear) + "_to_" + str(endYear-1) + ".txt", "w")
	first_year = True
	dividing_line = ""
	decade_divider = ""
	s = ""
	
	old_length_s = 0
	length_current_month = 0
	month_header = ""
	title = ""

	data = dict()
	for year in range(startYear, endYear):
		s = "|"
		# data[year] = dict()
		for month in months:
			old_length_s = len(s)

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

			# print len(s)
			if month is "February" and len(s) is 223:
				s += "    "
			s += " |"

			if first_year is True:
				length_current_month = len(s) - old_length_s 
				blankspace = (length_current_month/2) - len(month)/2
				if len(month)%2 is not 0:
					month_header += " "*blankspace + month + " "*(blankspace-1)
				else:
					month_header += " "*blankspace + month + " "*blankspace

			if month is "June":
				s += "|  " + str(year) + "  ||"
				month_header += "            "
				actual_title = str(startYear) + " to " + str(endYear-1)
				title = " "*((len(s)-7)-(len(actual_title)/2 -1 )) + actual_title
			
		# print s

		if first_year is True:
			first_year = False
			writer.write(title)
			writer.write("\n"*5)
			writer.write(month_header)
			writer.write("\n"*3)
			for c in s:
				if c is not "|":
					dividing_line += "-"
					decade_divider += "="
				else:
					dividing_line += c
					decade_divider += c

		if str(year)[-1] is "0":
			writer.write(decade_divider)
			writer.write("\n")
			writer.write(decade_divider)
		else:
			writer.write(dividing_line)
		writer.write("\n")
		writer.write(s)
		writer.write("\n")

	writer.write(dividing_line)
	writer.write("\n"*2)
	writer.write("* = sunday")
	writer.write("\n"*2)
	writer.write("inspired by On Kawara\nre-created by Leon Eckert")
	writer.close()




def Main():
	try: 
		print 
		startYear = int(sys.argv[1])
		year_interval = int(sys.argv[2])
		endYear = startYear + year_interval 
		getDaysData(startYear, endYear)
		print "[+] done, find the output in this file:", str(startYear) + "_to_" + str(endYear-1) + ".txt"
		print "[?] contact me if you have questions about how to turn it into a large .pdf to print\n\nleoneckert@me.com\n" 

	except:
		print "\nuse the script with a command like this:\n"
		print "python multi_year_calendar.py 1990 100"
		print "                               ^    ^ "
		print "                               |    | "
		print "             [year to start from]  [number of years to be included in the calendar]\n\n"
	

if __name__ == '__main__':
    Main()




