## MAIN APP
##
##

import numpy as np
import matplotlib.pyplot as plt

from week import Week
from dataset import DataSet

def inputData(dataset):
    i=0
    done = False
    while(not done):
        try:
            x = int(input("Insert a value : \n" ) ) 
        except ValueError:
            print("Do you want to quit? (y/n) : \n ")
            finish = str(input(" "))
            if (finish == 'y'):
                 done = True
                 break
            continue
             
        try:
           
                dataset.weeks[i].insert_node(x)
        
        except ValueError:
            dataset.insert()
            i+=1
            
    
          
            
      





# initialize the DataSet

data = DataSet()

# The x axis will always be 1-7
# this indicates the days of the week

#x = np.array([1, 2, 3])

# y = data.weeks[0].nodes

## TEST SHIT

week = Week()

data.insert_week(week)
inputData(data)

for week in data.weeks:
    y = week.nodes
    x = np.arange(y.size)+1
    print(y)
    plt.scatter(x,y)
    plt.plot(x,y)

   
    
plt.show()
    






