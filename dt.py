from datetime import datetime

class DateTime(datetime):
	def as_object(string):
		year         = int(string[0:4])
		month        = int(string[5:7])
		day          = int(string[8:10])
		hour         = int(string[11:13])
		minutes      = int(string[14:16])
		seconds      = int(string[17:19])
		milliseconds = int(string[20:len(string)])

		return DateTime(year, month, day, hour, minutes, seconds, milliseconds)