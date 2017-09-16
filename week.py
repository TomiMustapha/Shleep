## Week class
##
## Each week is a list of fixed size 7 of nodes
## Represents a week in which we log hours of sleep
## We can then combine weeks into a matrix to be represented graphically

import numpy as np

class Week():

    def __init__(self):

        self.nodes = np.array([])

    def insert_node(self, node):
        if (not type(node) == Node):
            raise TypeError("Not a node.")
        elif (nodes.size > 7):
            raise ValueError("Week has exceeded 7")
        else:
            self.nodes.append(node)

    def print(self):
        print(nodes)

        

        

    
