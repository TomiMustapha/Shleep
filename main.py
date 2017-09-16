## MAIN APP
##
##

import numpy as np
import matplotlib.pyplot as plt

from week import Week
from dataset import DataSet

# initialize the DataSet

data = DataSet()

# The x axis will always be 1-7
# this indicates the days of the week

x = np.array([1, 2, 3])

# y = data.weeks[0].nodes

## TEST SHIT

week = Week()

week.insert_node(1)
week.insert_node(2)
week.insert_node(3)

data.insert_week(week)

y = data.weeks[0].nodes


plt.scatter(x,y)
plt.show()


