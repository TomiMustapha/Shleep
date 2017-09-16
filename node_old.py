## Node class
##
## Each node represents a point on the scatter plot (indicating hours slept)
##
## Fields:
##    day - day of the week (int 0 - 6)
##    hours - hours slept
##    week - week (int, for logging purposes (int 0 - 51)

class Node():

    #Constructor
    def __init__(self, day, hours, week):
        
        if (day >= 7 or day < 0):
            raise ValueError("Day must be between 0 and 6, inclusive")
        else:
            self.day = day

        if (hours < 0):
            raise ValueError("Hours cannot be negative")
        else:
            self.hours = hours

        if (week > 51 or week < 0):
            raise ValueError("Week must be between 0 and 51, inclusive")
        else:
            self.week = week

    def get_day(self):
        return self.day

    def get_hours(self):
        return self.hours

    def get_week(self):
        return self.weeks

    def edit_day(self, day):
        if (day >= 7 or day < 0):
            raise ValueError("Day must be between 0 and 6, inclusive")
            print("Day must be between 0 and 6, inclusive")
        else:
            self.day = day

    def edit_hours(self, hours):
        if (hours < 0):
            raise ValueError("Hours cannot be negative")
        else:
            self.hours = hours

    def edit_week(self, week):
        if (week > 51 or week < 0):
            raise ValueError("Week must be between 0 and 51, inclusive")
        else:
            self.week = week

    def print(self):
        print("Day = " + str(self.day) + ", Hours = " + str(self.hours) + ", Week = " + str(self.week))
        
