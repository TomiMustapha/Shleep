## Data Set class
## 
## Each data set is an array of weeks
## So every entry is an array of nodes

import numpy as np
from week import Week

class DataSet():
    
    def __init__(self):
        self.weeks = np.array([])
        
    def insert_week(self, week):
        self.weeks = np.append(self.weeks, week)
        
    def insert(self):
        newWeek = Week()
        self.insert_week(newWeek)
            
        
    def print(self):
        i = 1
        for week in self.weeks:
            print("Week: " + str(i))
            print(week.nodes)
            i+=1
        
    

