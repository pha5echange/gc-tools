# datetime calculator v0.1
# Aug 26 2015
# by jmg@phasechange.info
# takes 2 datetime objects and outputs the difference

import datetime as dt

versionNumber = ("a01")

# ..and begin..
print
print ("AJW: Date-Calc-Thingy | " + "Version: " + versionNumber + " | Starting" + '\n')

# make start and end year the same, and current
year = 2015

# make seconds zero as it doesn't matter
second = 0

# user input for start variables 
print
print ("INPUT START PARAMETERS: ")
month1 = int(input ("enter the start month (1-12): "))
day1 = int(input ("enter the start day (1-31): "))
hour1 = int(input ("enter the start hour (24 hour clock: 0-23): "))
minute1 = int(input ("enter the start minute (0-59): "))

# user input for end variables
print
print ("INPUT END PARAMETERS: ")
month2 = int(input ("enter the end month (1-12): "))
day2 = int(input ("enter the end day (1-31): "))
hour2 = int(input ("enter the end hour (24 hour clock: 0-23): "))
minute2 = int(input ("enter the end minute (0-59): "))

# assign variables to datetime objects
start = dt.datetime(year,month1,day1,hour1,minute1,second)
end = dt.datetime(year,month2,day2,hour2,minute2,second)

# calculate various results
result_seconds = float ((end-start).total_seconds())
result_minutes = float (result_seconds / 60)
result_hours = float (result_minutes / 60)
result_days = float (result_hours / 24)
result_weeks = float (result_days / 7)

# output for checking
print
print ("OUTPUT FOR CHECKING: ")
print ("Year: ", year)
print ("Start month: ", month1)
print ("Start day: ", day1)
print ("Start hour: ", hour1)
print ("Start minute: ", minute1)
print ("End month: ", month2)
print ("End day: ", day2)
print ("End hour: ", hour2)
print ("End minute: ", minute2)
print ("Second: ", second)

# output results in various forms
print
print ("RESULTS: ")
print ("Seconds: ", result_seconds)
print ("Minutes: ", result_minutes)
print ("Hours: ", result_hours)
print ("Days: ", result_days)
print ("Weeks: ", result_weeks)

# write to screen
print
print ("RUN INFORMATION: ")
print ("AJW: Date-Calc-Thingy")
print ("Version: " + versionNumber + '\n')
