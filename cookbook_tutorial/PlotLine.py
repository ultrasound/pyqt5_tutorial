#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as graph

x = [10, 20, 30]
y = [20, 40, 60]
yesrs = ['2016', '2017', '2018']
profit = [70, 90, 80]

# graph.title('Plotting a Line')
# graph.xlabel('x - axis')
# graph.ylabel('y - axis')
# graph.plot(x, y)
# graph.show()
graph.bar(yesrs, profit)
graph.title('Growth in Business')
graph.plot(100)
graph.show()