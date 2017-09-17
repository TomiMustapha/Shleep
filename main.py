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
            x = int(input("Insert hours of sleep : \n" ) ) 
        except ValueError:
            print("Quit and show plot? (y/n) : \n ")
            finish = str(input(" "))
            if (finish == 'y'):
                 done = True
                 break
            continue
             
        try:
           
                dataset.weeks[i].insert_node(x)
        
        except ValueError:
            dataset.insert(x)
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

i = 1
for week in data.weeks:
    y = week.nodes
    x = np.arange(1, y.size+1, 1)
    #print(y)
    plt.scatter(x,y)
    lines = plt.plot(x,y)
    plt.setp(lines, label="Week " + str(i))
    i+=1
    
# Ideal sleep schedule to compare to
ideal_y = np.array([8, 8, 8, 8, 8, 8, 8])
ideal_x = np.arange(ideal_y.size)+1
ideal_err = 1
#ideal_err_bar = plt.errorbar(ideal_x, ideal_y, yerr=ideal_err)
#ideal_err_bar[-1][0].set_linestyle('--')
ideal = plt.plot(ideal_x, ideal_y)
plt.setp(ideal, label="Ideal Schedule")


plt.title("Sleep Distribution")
plt.xlabel("Day of the Week")
plt.ylabel("Hours of Sleep")
plt.legend(loc='best')

   
    
plt.show()
    






