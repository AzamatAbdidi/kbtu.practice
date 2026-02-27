#1 Import the datetime module and display the current date:

import datetime
x = datetime.datetime.now()
print(x)

#2 Import the datetime module and display the current date:

import datetime
x = datetime.datetime.now()
print(x)

#3 The datetime() class requires three parameters to create a date: year, month, day.

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)


#4 The method is called strftime(), and takes one parameter,
#  format, to specify the format of the returned string
# Display the name of the month:

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# "%a	Weekday, short version"
# "%A	Weekday, full version"
# "%w	Weekday as a number 0-6, 0 is Sunday"
# "%d	Day of month 01-31"
# "%b	Month name, short version"
# "%B	Month name, full version"
# "%m	Month as a number 01-12"
# "%y	Year, short version, without century"
# "%Y	Year, full version"
# "%H	Hour 00-23"
# "%I	Hour 00-12"
# "%p	AM/PM"
# "%M	Minute 00-59"
# "%S	Second 00-59"
# "%x	Local version of date"
# "%X	Local version of time"

