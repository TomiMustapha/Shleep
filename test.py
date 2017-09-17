
from week import Week
from dataset import DataSet

node1 = Node(5)
node2 = Node(20)
node3 = Node(20)
node4 = Node(20)
node5 = Node(20)
node6 = Node(20)
node7 = Node(20)


week = Week()

week.insert_node(node1)
week.insert_node(node2)
week.insert_node(node3)
week.insert_node(node4)
week.insert_node(node5)
week.insert_node(node6)
week.insert_node(node7)

dataset = DataSet()

dataset.insert_week(week)

week2 = Week()

week2.insert_node(node2)
week2.insert_node(node1)

dataset.insert_week(week2)

dataset.print()

