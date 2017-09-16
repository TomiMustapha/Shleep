## Data Set class
## 
## Each data set is an array of weeks
## So every entry is an array of nodes

import numpy as np
from node import Node
from week import Week

class DataSet():
    
    def __init__(self):
        self.weeks = np.array([])
        
    def insert_week(self, week):
        self.weeks = np.append(self.weeks, week)
        
    def print(self):
        i = 1
        for week in self.weeks:
            print("Week: " + str(i))
            week.print()
            i+=1
        
    

