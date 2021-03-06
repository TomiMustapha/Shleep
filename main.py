## MAIN APP
##
##

import numpy as np
import matplotlib.pyplot as plt

from week import Week
from dataset import DataSet

def inputData(dataset):
    i = np.size(dataset.weeks)-1
    done = False
    while(not done):
        try:
            x = int(input("Insert hours of sleep (Press Enter to Quit) : \n" ) ) 
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
         
def getDayAverage(dataset,day):
    average = np.array([])
    for i in range(0, np.size(dataset.weeks)):
        if(np.size(dataset.weeks[i].nodes) > day):
            average= np.append(average,dataset.weeks[i].nodes[day])
        else:
            break
    return np.average(average)            
    

# initialize the DataSet

data = DataSet()

file = np.load('data.npy')

for week in file:
   data.insert_week(week)
    
   
print("Previous data: \n")
data.print()
print("\n")

# The x axis will always be 1-7
# this indicates the days of the week

inputData(data)

np.save('data.npy', data.weeks)

i = 1
for week in data.weeks:
    y = week.nodes
    x = np.arange(1, y.size+1, 1)
    #print(y)
    plt.scatter(x,y)
    lines = plt.plot(x,y)
    plt.setp(lines, label="Week " + str(i))
    i+=1

   
    
    
    
#Create an array that keeps track of the average sleep per week   
averageSleep = np.array([])    
for week in data.weeks:
    x = np.average(week.nodes)
    averageSleep = np.append(averageSleep,x)
#Calculate the average sleep over all the weeks    
averageSleepTotal = np.average(averageSleep) 
#Calculate the average sleep for each day  
averagePerDay = np.array([])
for i in range (0,7):
    x = getDayAverage(data,i)
    averagePerDay = np.append(averagePerDay, x)
print(averagePerDay)    
#print(averageSleep)
#print(averageSleepTotal)
# Ideal sleep schedule to compare to

ideal_y = np.array([8, 8, 8, 8, 8, 8, 8])
ideal_x = np.arange(ideal_y.size)+1
ideal_err = 1
ideal = plt.plot(ideal_x, ideal_y)
xDay = np.arange(1,8) 
plt.setp(ideal, label="Ideal Schedule")
perDay = plt.plot(xDay,averagePerDay)
plt.setp(perDay, label="Average Sleep Per Day")


plt.title("Sleep Distribution")
plt.xlabel("Day of the Week")
plt.ylabel("Hours of Sleep")
plt.legend(loc='best')
plt.figtext(0.5, .95, 'Your Average Sleep is '+str(round(averageSleepTotal,2))+' hours per day', horizontalalignment='right')

   
    
plt.show()  






