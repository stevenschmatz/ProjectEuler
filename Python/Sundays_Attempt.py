"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

class Sundays:
		
	def Get_Day(self, day_number):
		weekday_number = day_number%7
		weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
		return weekdays[weekday_number]

	def Is_Leap_Year(self, year_number):
		if year_number % 400 == 0:
			return False
		elif year_number % 4 == 0:
			return True
		return False

	def Days_In_Year(self, year_number):
		if self.Is_Leap_Year(year_number):
			return 366
		return 365

	def Get_Total_Days(self, year_begin, year_end):
		days = 0
		year_total = year_end-year_begin + 1 #considering inclusive
		for year in range(1, year_total+ 1):
			days += self.Days_In_Year(year)
		return days

	def Year_From_Day(self, day_number, initial_year = 1901):
		days_elapsed = 0
		years_elapsed = initial_year
		while day_number > 0:
			if days_elapsed == self.Days_In_Year(years_elapsed):
				years_elapsed += 1
				days_elapsed = 0
			day_number -= 1
			days_elapsed += 1
		return years_elapsed

	def Setup_Month_List(self, day_number):
		months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if self.Is_Leap_Year(self.Year_From_Day(day_number, 1901)):
			months[1] = 29
		return months

	def Month_From_Day(self, day_number):
		day = day_number - self.Get_Total_Days(1901, self.Year_From_Day(day_number)-1)
		month = 0
		month_list = self.Setup_Month_List(day_number)
		while month<12:
			if month == 11:
				return month
			if day - month_list[month] <= 0:
				return month
			day -= month_list[month]
			month += 1

	def Is_First_Of_Month(self, day_number):
		if day_number == 0:
			return True
		if self.Month_From_Day(day_number+1)>self.Month_From_Day(day_number):
			return True
		return False

	def Solve(self):
		day_count = 0
		for day in range(self.Get_Total_Days(1901,2000)):
			if (self.Get_Day(day)=='Sunday') and (self.Is_First_Of_Month(day)==True):
				day_count += 1
		return day_count

MySolution = Sundays()
print MySolution.Solve()
