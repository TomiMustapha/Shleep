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
    def __init__(self, hours):

        if (not self.isNum(hours) or hours < 0):
            raise ValueError("Hours cannot be negative or non-numeric")
        else:
            self.hours = hours

    def get_hours(self):
        return self.hours

    def edit_hours(self, hours):
        if (hours < 0):
            raise ValueError("Hours cannot be negative")
        else:
            self.hours = hours

    def print(self):
        print("Hours = " + str(self.hours))

    def isNum(self, value):
        return str(value).isnumeric()
        
